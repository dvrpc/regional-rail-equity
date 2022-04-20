from regional_rail_equity import db
from regional_rail_equity.database.config.station_summary_config import (
    station_summary_files,
)

query_template = """
    drop table if exists NEW_TABLENAME;

    create table NEW_TABLENAME as
    
    with joined_model_with_tod as(
        select *, st_transform(a.geom, 4326) 
        from model_rr_station_stoppoints a
        right join building_on_our_strengths_stations b
        on st_dwithin(a.geom,b.geom,110)
        inner join TABLENAME_PLACEHOLDER c 
        on a.no = c.stoppointno
        where b.type = 'Commuter Rail' and "operator" = 'SEPTA')
    select station, "no", lucontext, type_1, passboardap as "boardings", passalightap as "alights", "st_transform"  from joined_model_with_tod
    order by station
     """


if __name__ == "__main__":

    for scenario in station_summary_files:
        existing_raw_table = scenario.sql_tablename
        new_tablename = existing_raw_table.replace("public.", "computed.")
        query = query_template.replace(
            "TABLENAME_PLACEHOLDER", scenario.sql_tablename
        ).replace("NEW_TABLENAME", new_tablename)
        db.execute(query)
