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
    MergeConfig(
        raw_pathlegs_table="existing_2019md_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.2019ec_md",
        new_tablename="computed.existing2019md_path_legs_with_assignment",
    ),
    MergeConfig(
        raw_pathlegs_table="existing_2019pm_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.2019ec_pm",
        new_tablename="computed.existing2019pm_path_legs_with_assignment",
    ),
    MergeConfig(
        raw_pathlegs_table="existing_2019nt_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.2019ec_nt",
        new_tablename="computed.existing2019nt_path_legs_with_assignment",
    ),
    # Scenario 1 ---------------------------------------------------------------
    MergeConfig(
        raw_pathlegs_table="scenario1_2045am_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s1_am",
        new_tablename="computed.s1_am_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario1_2045md_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s1_md",
        new_tablename="computed.s1_md_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario1_2045pm_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s1_pm",
        new_tablename="computed.s1_pm_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario1_2045nt_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s1_nt",
        new_tablename="computed.s1_nt_joined",
    ),
    # Scenario 2 ---------------------------------------------------------------
    MergeConfig(
        raw_pathlegs_table="scenario2_2045am_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s2_am",
        new_tablename="computed.s2_am_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario2_2045md_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s2_md",
        new_tablename="computed.s2_md_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario2_2045pm_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s2_pm",
        new_tablename="computed.s2_pm_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario2_2045nt_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s2_nt",
        new_tablename="computed.s2_nt_joined",
    ),
    # Scenario 3 ---------------------------------------------------------------
    MergeConfig(
        raw_pathlegs_table="scenario3_2045am_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s3_am",
        new_tablename="computed.s3_am_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario3_2045md_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s3_md",
        new_tablename="computed.s3_md_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario3_2045pm_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s3_pm",
        new_tablename="computed.s3_pm_joined",
    ),
    MergeConfig(
        raw_pathlegs_table="scenario3_2045nt_home_to_dest_zone_fullpath",
        assigned_parkandride_table="computed.s3_nt",
        new_tablename="computed.s3_nt_joined",
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
