"""
Transform the raw path leg listing table into a summarized version that includes:
    - one row per TAZ origin
    - total trip origins starting in that TAZ
    - weighted average of trip length in minutes
    - weighted average of trip fare cost
    - joined demographic data

For each configured path leg table, use the following naming scheme:
    - If the origina name is: public.existing_2019am_home_to_dest_zone_fullpath
    - Then the summary will be named: computed.summary_of_existing_2019am_home_to_dest_zone_fullpath
"""

from dataclasses import dataclass

from regional_rail_equity import db


@dataclass
class SummarizeTripTableConfig:

    # name of the SQL table that has one row per path leg trip (including parknrides)
    sql_tablename: str

    # name of the output table with one row per zone, with demographic attributes
    new_tablename: str


CONFIG = [
    SummarizeTripTableConfig(
        sql_tablename="computed.existing2019am_path_legs_with_assignment",
        new_tablename="aggregated.existing2019am_path_legs_with_assignment",
    )
]

query_template = """
    drop table if exists NEW_TABLENAME;

    create table NEW_TABLENAME as

    with trip_data as (
        select
            origzoneno,
            sum(odtrips) as total_origins,
            sum(minutes * odtrips) / sum(odtrips) as weighted_avg_time,
            sum(faretw * odtrips) / sum(odtrips) as weighted_avg_fare
        from TABLENAME_PLACEHOLDER
        where origzoneno::int < 90000
        group by origzoneno 
    )
    select d.*, s.* 
    from trip_data d
    left join ctpp.summary s
    on d.origzoneno = s.taz_id::text
"""


if __name__ == "__main__":

    for table in CONFIG:
        query = query_template.replace("TABLENAME_PLACEHOLDER", table.sql_tablename).replace(
            "NEW_TABLENAME", table.new_tablename
        )
        db.execute(query)
