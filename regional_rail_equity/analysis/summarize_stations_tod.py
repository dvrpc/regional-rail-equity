from regional_rail_equity import db
from regional_rail_equity.database.config.station_summary_config import (
    station_summary_files,
)
from regional_rail_equity.database.config.env_vars import GDRIVE_PROJECT_FOLDER
from datetime import datetime
import pandas as pd

query_template = """
    drop table if exists NEW_TABLENAME;

    create table NEW_TABLENAME as
    
    with joined_model_with_tod as(
        with booss as(
        select * from building_on_our_strengths_stations booss where type = 'Commuter Rail' and "operator" = 'SEPTA'
    )
        select 
            b.station,
            a.name, 
            no, 
            c.passboardap as boardings, 
            c.passalightap as alights, 
            b.lucontext, 
            b.type_1 as dev_type,
            b.existingor as existing_tod_orientation, 
            b.futurepote as future_tod_potential, 
            b.exo_quad as existing_orientation_quad, 
            b.fp_quad as future_potential_quad, 
            b.quad as combined_potential,
            st_transform(a.geom, 4326) as geom 
        from model_rr_station_stoppoints a
        left join booss b
            on st_dwithin(a.geom,b.geom,110)
        right join TABLENAME_PLACEHOLDER c 
            on a.no = c.old_num
        order by station)
    select * from joined_model_with_tod
     """

query2 = """
    drop table if exists computed.station_summary_all;
    create table computed.station_summary_all as(
        select 
            distinct s1am.name, 
            nobuildam.boardings as nobuildam_boardings, 
            nobuildam.alights as nobuildam_alights, 
            nobuildmd.boardings as nobuildmd_boardings,
            nobuildmd.alights as nobuildmd_alights,
            nobuildpm.boardings as nobuildpm_boardings,
            nobuildpm.alights as nobuildpm_alights,
            nobuildnt.boardings as nobuildnt_boardings,
            nobuildnt.alights as nobuildnt_alights,


            s1am.boardings as s1am_boardings, 
            s1am.alights as s1am_alights, 
            s1md.boardings as s1md_boardings,
            s1md.alights as s1md_alights,
            s1pm.boardings as s1pm_boardings,
            s1pm.alights as s1pm_alights,
            s1nt.boardings as s1nt_boardings,
            s1nt.alights as s1nt_alights,
            s2am.boardings as s2am_boardings,
            s2am.alights as s2am_alights,
            s2md.boardings as s2md_boardings,
            s2md.alights as s2md_alights,
            s2pm.boardings as s2pm_boardings,
            s2pm.alights as s2pm_alights,
            s2nt.boardings as s2nt_boardings,
            s2nt.alights as s2nt_alights,
            s3am.boardings as s3am_boardings,
            s3am.alights as s3am_alights,
            s3md.boardings as s3md_boardings,
            s3md.alights as s3md_alights,
            s3pm.boardings as s3pm_boardings,
            s3pm.alights as s3pm_alights,
            s3nt.boardings as s3nt_boardings,
            s3nt.alights as s3nt_alights,
            s1am.lucontext, 
            s1am.dev_type, 
            s1am.combined_potential, 
            s1am.geom 
            from computed.station_summary_2045s1_am s1am
        
        full outer join computed.station_summary_2045nobuild_am nobuildam 
        on s1am.no = nobuildam.no        
        full outer join computed.station_summary_2045nobuild_md nobuildmd 
        on s1am.no = nobuildmd.no
        full outer join computed.station_summary_2045nobuild_pm nobuildpm
        on s1am.no = nobuildpm.no
        full outer join computed.station_summary_2045nobuild_nt nobuildnt
        on s1am.no = nobuildnt.no

    
        full outer join computed.station_summary_2045s1_md s1md 
        on s1am.no = s1md.no
        full outer join computed.station_summary_2045s1_pm s1pm
        on s1am.no = s1pm.no
        full outer join computed.station_summary_2045s1_nt s1nt
        on s1am.no = s1nt.no
        full outer join computed.station_summary_2045s2_am s2am
        on s1am.no = s2am.no
        full outer join computed.station_summary_2045s2_md s2md
        on s1am.no = s2md.no
        full outer join computed.station_summary_2045s2_pm s2pm
        on s1am.no = s2pm.no
        full outer join computed.station_summary_2045s2_nt s2nt
        on s1am.no = s2nt.no
        full outer join computed.station_summary_2045s3a_am s3am
        on s1am.no = s3am.no
        full outer join computed.station_summary_2045s3a_md s3md
        on s1am.no = s3md.no
        full outer join computed.station_summary_2045s3a_pm s3pm
        on s1am.no = s3pm.no
        full outer join computed.station_summary_2045s3a_nt s3nt
        on s1am.no = s3nt.no
        order by name);
"""

query3 = """select * from computed.station_summary_all"""

if __name__ == "__main__":

    for scenario in station_summary_files:
        existing_raw_table = scenario.sql_tablename
        new_tablename = existing_raw_table.replace("public.", "computed.")
        query = query_template.replace(
            "TABLENAME_PLACEHOLDER", scenario.sql_tablename
        ).replace("NEW_TABLENAME", new_tablename)
        db.execute(query)

db.execute(query2)

now = datetime.now()
now = now.strftime("%Y-%M-%d %H:%M:%S")
output_excel_filepath = (
    GDRIVE_PROJECT_FOLDER
    / f"Station summary output {now.replace(':','-').replace('.', '-')}.xlsx"
)
with pd.ExcelWriter(output_excel_filepath) as writer:
    df = db.df(query3)
    df.to_excel(writer)
