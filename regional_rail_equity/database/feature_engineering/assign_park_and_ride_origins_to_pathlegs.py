import pandas as pd
import random
from tqdm import tqdm
from regional_rail_equity import db


PATH_LEGS_TABLE = "existing_2019am_home_to_dest_zone_fullpath"
PARKNRIDE_TABLE = "existing_2019am_home_to_station_2152"
NEW_TABLENAME = "test_pnr_assignment"


def assign_origin_zone_to_parkandride_path_leg_data(
    zoneid: int,
    path_legs_table: str = PATH_LEGS_TABLE,
    pnr_table: str = PARKNRIDE_TABLE,
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
    print("\t -> Making bookends")
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
    print("\t -> Exploding table")

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

    # Assign a "true_origzoneno" to each row in the exploded df
    print("\t -> Assigning new zones")

    exploded_df["true_origzoneno"] = ""
    for idx, row in tqdm(exploded_df.iterrows(), total=exploded_df.shape[0]):

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

    return exploded_df


if __name__ == "__main__":

    # Get a list of all Park&Ride zone IDs
    park_and_ride_zones = db.query_as_list_of_singletons(
        f"""
        select distinct origzoneno
        from {PATH_LEGS_TABLE}
        where origzoneno::int >= 90000
    """
    )

    dfs = []

    for pnrid in park_and_ride_zones:
        print(f"PROCESSING PARK AND RIDE ZONE: {pnrid}")
        df = assign_origin_zone_to_parkandride_path_leg_data(pnrid)
        dfs.append(df)

        print("\t", df.shape)

    merged_df = pd.concat(dfs)

    db.import_dataframe(merged_df, tablename=NEW_TABLENAME)
