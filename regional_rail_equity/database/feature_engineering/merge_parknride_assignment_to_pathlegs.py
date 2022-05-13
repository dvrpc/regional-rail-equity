from regional_rail_equity import db
from dataclasses import dataclass


@dataclass
class MergeConfig:

    # name of the raw table imported from the att file e.g. existing_2019am_home_to_dest_zone_fullpath
    raw_pathlegs_table: str

    # name of the computed / assigned parkandride table i.e. computed.s1_am
    assigned_parkandride_table: str

    # name of the new table (also goes into computed folder). basically path legs plus pnr assignment
    new_tablename: str


CONFIG = [
    MergeConfig(
        raw_pathlegs_table="existing_2019am_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.test_pnr_assignment",
        new_tablename="computed.existing2019am_path_legs_with_assignment",
    ),
]

query_template = f"""
    drop table if exists NEW_TABLENAME;

    create table NEW_TABLENAME as 

    with non_parkandride as (
        select
            origzoneno,
            destzoneno,
            odtrips,
            faretw,
            minutes,
            null as via_parknride
        from RAW_PATHLEG
        where origzoneno::int < 90000
    ),
    parkandride as (
        select
            true_origzoneno as origzoneno,
            destzoneno,
            sum(odtrips) as odtrips,
            faretw,
            minutes,
            origzoneno as via_parknride
        from ASSIGNED_PNR
        group by
            true_origzoneno, destzoneno, faretw, minutes, origzoneno
    )
    select * from non_parkandride 
    union select * from parkandride
"""

if __name__ == "__main__":

    for table in CONFIG:
        query = (
            query_template.replace("RAW_PATHLEG", table.raw_pathlegs_table)
            .replace("ASSIGNED_PNR", table.assigned_parkandride_table)
            .replace("NEW_TABLENAME", table.new_tablename)
        )
        db.execute(query)
