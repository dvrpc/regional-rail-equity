import pandas as pd
from functools import reduce
from datetime import datetime
from dataclasses import dataclass

from regional_rail_equity import db
from regional_rail_equity.database.config.env_vars import GDRIVE_PROJECT_FOLDER
from regional_rail_equity.database.config.path_legs_config import path_legs_config


@dataclass
class SummarizeDemographicsConfig:

    # name of existing sql tablename that has one row per taz with demographics
    aggregated_tablename: str

    # ID of the scenario, used to create excel tabname
    scenario_name: str


summary_tables = [
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.existing2019am_path_legs_with_assignment",
        scenario_name="existing2019am",
    ),
    # Scenario 1 ------------------------------------
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s1_am",
        scenario_name="scenario1am",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s1_md",
        scenario_name="scenario1md",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s1_pm",
        scenario_name="scenario1pm",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s1_nt",
        scenario_name="scenario1nt",
    ),
    # Scenario 2-------------------------------------
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s2_am",
        scenario_name="scenario2am",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s2_md",
        scenario_name="scenario2md",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s2_pm",
        scenario_name="scenario2pm",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s2_nt",
        scenario_name="scenario2nt",
    ),
    # Scenario 3-------------------------------------
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s3_am",
        scenario_name="scenario3am",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s3_md",
        scenario_name="scenario3md",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s3_pm",
        scenario_name="scenario3pm",
    ),
    SummarizeDemographicsConfig(
        aggregated_tablename="aggregated.s3_nt",
        scenario_name="scenario3nt",
    ),
]


demographic_columns = [
    "nonwhite",
    "pct_non_english",
    "nonmotorized",
    "below_100pct_poverty",
]

# Travel time query gets total trips grouped by demographic bucket number (mm edit: buckets are now 1% instead of 10)
total_trips_query = """

select BUCKET_NAME::numeric(10,0) as bucket, sum(total_origins) as BUCKET_NAME_trips
    from
        SUMMARY_TABLE
    group by BUCKET_NAME::numeric(10,0) 
    order by bucket

"""

# Travel time query is similar to the total trips query, but uses a weighted average
travel_time_query = """

select BUCKET_NAME::numeric(10,0) as bucket, sum(total_origins * weighted_avg_time) / sum(total_origins) as BUCKET_NAME_time
from
    SUMMARY_TABLE
group by BUCKET_NAME::numeric(10,0) 
order by bucket

"""

# Fare query is exactly the same as travel time, but uses the fare column instead of time
fare_query = travel_time_query.replace(
    "weighted_avg_time", "weighted_avg_fare"
).replace("BUCKET_NAME_time", "BUCKET_NAME_fare")

if __name__ == "__main__":
    # Run all queries for all tables
    tabs = []

    for table in summary_tables:
        dfs = []

        for query_template in [total_trips_query, travel_time_query, fare_query]:
            for demo_col in demographic_columns:
                # Make the query by dropping in the data tablename and the demographic bucket to use
                query = query_template.replace(
                    "SUMMARY_TABLE", table.aggregated_tablename
                ).replace("BUCKET_NAME", demo_col)
                # Run the query and save it to the list
                df = db.df(query)
                dfs.append(df)

        # Merge all 12 query outputs into a single summary table
        merged_df = reduce(
            lambda x, y: pd.merge(x, y, on="bucket", how="outer"), dfs
        ).sort_values(by=["bucket"])

        tabs.append(
            {
                "sheetname": table.scenario_name,
                "df": merged_df,
            }
        )

    # Write output to Excel file and save to Google Drive
    now = datetime.now()
    now = now.strftime("%Y-%M-%d %H:%M:%S")
    output_excel_filepath = (
        GDRIVE_PROJECT_FOLDER
        / f"Equity Analysis output {now.replace(':','-').replace('.', '-')}.xlsx"
    )
    with pd.ExcelWriter(output_excel_filepath) as writer:
        for tab in tabs:
            tab["df"].to_excel(writer, sheet_name=tab["sheetname"])
