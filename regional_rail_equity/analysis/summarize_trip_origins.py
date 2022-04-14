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

from regional_rail_equity import db
from regional_rail_equity.database.config.path_legs_config import path_legs_config

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

    for table in path_legs_config:
        existing_raw_table = table["sql_tablename"]
        new_tablename = existing_raw_table.replace("public.", "computed.summary_of_")
        query = query_template.replace("TABLENAME_PLACEHOLDER", table["sql_tablename"]).replace(
            "NEW_TABLENAME", new_tablename
        )
        db.execute(query)
