import pandas as pd
from functools import reduce

from regional_rail_equity import db
from regional_rail_equity.database.config.path_legs_config import path_legs_config

summary_tables = [
    table["sql_tablename"].replace("public.", "computed.summary_of_") for table in path_legs_config
]


demographic_columns = [
    "bucket_nonwhite",
    "bucket_pct_non_english",
    "bucket_non_motorized",
    "bucket_below_100pct_poverty",
]

# Travel time query gets total trips grouped by demographic bucket number
total_trips_query = """
    select
        case
            when BUCKET_NAME is not null then BUCKET_NAME
            else 999 end as bucket,
        sum(total_origins) as BUCKET_NAME_origins
    from
        SUMMARY_TABLE
    group by BUCKET_NAME 
    order by BUCKET_NAME 
"""

# Travel time query is similar to the total trips query, but uses a weighted average
travel_time_query = """
    select
        case
            when BUCKET_NAME is not null then BUCKET_NAME
            else 999 end as bucket,
        sum(total_origins * weighted_avg_time) / sum(total_origins) as BUCKET_NAME_time
    from
        SUMMARY_TABLE
    group by BUCKET_NAME 
    order by BUCKET_NAME 
"""

# Fare query is exactly the same as travel time, but uses the fare column instead of time
fare_query = travel_time_query.replace("weighted_avg_time", "weighted_avg_fare").replace(
    "BUCKET_NAME_time", "BUCKET_NAME_fare"
)


# Run all queries for all tables, and write to Excel tab

tabs = []

for table in path_legs_config:
    computed_tablename = table["sql_tablename"].replace("public.", "computed.summary_of_")

    dfs = []
    for query_template in [total_trips_query, travel_time_query, fare_query]:
        for demo_col in demographic_columns:
            query = query_template.replace("SUMMARY_TABLE", computed_tablename).replace(
                "BUCKET_NAME", demo_col
            )
            df = db.df(query)
            dfs.append(df)

    merged_df = reduce(lambda x, y: pd.merge(x, y, on="bucket", how="outer"), dfs).sort_values(
        by=["bucket"]
    )

    tabs.append(
        {
            "sheetname": table["summary_tabname"],
            "df": merged_df,
        }
    )

with pd.ExcelWriter("./result.xlsx") as writer:
    for tab in tabs:
        tab["df"].to_excel(writer, sheet_name=tab["sheetname"])
