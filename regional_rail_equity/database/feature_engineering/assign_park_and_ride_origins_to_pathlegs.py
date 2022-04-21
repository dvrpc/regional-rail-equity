from ipaddress import AddressValueError
import pandas as pd
import random
from rich.progress import (
    Progress,
    TimeElapsedColumn,
    SpinnerColumn,
    Column,
    BarColumn,
    TimeRemainingColumn,
)
from regional_rail_equity import db


PATH_LEGS_TABLE = "existing_2019am_home_to_dest_zone_fullpath"
PARKNRIDE_TABLE = "existing_2019am_home_to_station_2152"
NEW_TABLENAME = "test_pnr_assignment"


def assign_origin_zone_to_parkandride_path_leg_data(
    zoneid: int,
    progress: Progress,
    path_legs_table: str = PATH_LEGS_TABLE,
    pnr_table: str = PARKNRIDE_TABLE,
    new_tablename: str = NEW_TABLENAME,
) -> pd.DataFrame:
    """
    For a given Park&Ride zone id:
        - Find all of the home zones feeding into that parkNride,
          and the % of trips that originated there
        - Make an exploded path legs table where each row represents
          the smallest unit of trips possible (1 row == 0.001 trips)
        - Assign a home zone to each row using a random number and
          the percentages of trips originating in the true home zones

    Return the result as a pandas DataFrame
    """

    # Get all origins for a given PnR destination as % of total
    origin_query = f"""
        with trip_sum as (
            select sum(matvalue2152) as totaltrips
            from {pnr_table}
            where tozoneno = '{zoneid}'
        )
        select
            fromzoneno,
            matvalue2152,
            matvalue2152 / totaltrips * 100 as pct_of_total
        from {pnr_table}, trip_sum
        where tozoneno = '{zoneid}'
        order by matvalue2152 / totaltrips desc
    """
    true_origin_df = db.df(origin_query)

    # Assign bookends to each row
    true_origin_df["min"] = 0.0
    true_origin_df["max"] = 0.0

    minimum = 0
    maximum = 0
    for idx, row in true_origin_df.iterrows():
        minimum = maximum
        true_origin_df.at[idx, "min"] = minimum
        maximum = row["pct_of_total"] + minimum
        true_origin_df.at[idx, "max"] = maximum

    # Get all of the path legs that started at this PnR zone
    path_leg_query = f"""
        select origzoneno, destzoneno, odtrips, faretw, minutes
        from {path_legs_table}
        where origzoneno = '{zoneid}'
    """
    path_df = db.df(path_leg_query)

    # Make an 'exploded' dataframe where each row is 0.001 trips
    # i.e. a row that had 0.099 odtrips would become 99 rows
    newrows = []
    for idx, row in path_df.iterrows():
        rows_to_put_into_exploded_df = row["odtrips"] * 1000
        for _ in range(int(rows_to_put_into_exploded_df)):
            data = {
                "origzoneno": row["origzoneno"],
                "destzoneno": row["destzoneno"],
                "odtrips": 0.001,
                "qa_trips": row["odtrips"],
                "faretw": row["faretw"],
                "minutes": row["minutes"],
            }
            newrows.append(data)
    exploded_df = pd.DataFrame(newrows)

    # Assign a home TAZ to every exploded trip row
    new_zone_task = progress.add_task(f"[cyan]\t-> {zoneid}", total=exploded_df.shape[0])
    exploded_df["true_origzoneno"] = ""
    for idx, row in exploded_df.iterrows():

        matched_zoneid = None

        # Generate a random number for this row of data
        random_num = random.uniform(0.0, 100.0)

        # Find the origin zone number that has a range bookending this random number
        match_df = true_origin_df[
            (true_origin_df["min"] <= random_num) & (true_origin_df["max"] > random_num)
        ].reset_index()
        matched_zoneid = match_df.at[0, "fromzoneno"]

        # Assign the matched zoneid to the row's "true_origzoneno" cell
        exploded_df.at[idx, "true_origzoneno"] = str(matched_zoneid)

        progress.update(new_zone_task, advance=1)

    # Write the result to postgres
    db.import_dataframe(
        exploded_df, tablename=new_tablename, df_import_kwargs={"if_exists": "append"}
    )


if __name__ == "__main__":

    # Get a list of all Park&Ride zone IDs
    park_and_ride_zones = db.query_as_list_of_singletons(
        f"""
        select distinct origzoneno
        from {PATH_LEGS_TABLE}
        where   origzoneno::int >= 90000
            and origzoneno::int < 100000
            and origzoneno not in (
                select distinct origzoneno from {NEW_TABLENAME}
            )
            and origzoneno in (select distinct tozoneno from {PARKNRIDE_TABLE})
    """
    )

    dfs = []

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(bar_width=None, table_column=Column(ratio=1.5)),
        "[progress.percentage]{task.percentage:>3.3f}%",
        TimeRemainingColumn(),
        TimeElapsedColumn(table_column=Column(ratio=1)),
        expand=True,
    ) as progress:

        task1 = progress.add_task(
            "[green]Looping over all Park&Ride zones...", total=len(park_and_ride_zones)
        )

        print(f"PROCESSING {len(park_and_ride_zones)} zones")

        for pnrid in park_and_ride_zones:
            df = assign_origin_zone_to_parkandride_path_leg_data(pnrid, progress)
            progress.update(task1, advance=1)
