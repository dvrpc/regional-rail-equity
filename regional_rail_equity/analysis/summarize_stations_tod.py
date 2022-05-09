from regional_rail_equity import db
from regional_rail_equity.database.config.station_summary_config import (
    station_summary_files,
)

query_template = """
    drop table if exists NEW_TABLENAME;

    create table NEW_TABLENAME as
    
    with joined_model_with_tod as(
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
        right join building_on_our_strengths_stations b
            on st_dwithin(a.geom,b.geom,110)
        inner join TABLENAME_PLACEHOLDER c 
            on a.no = c.stoppointno
            where b.type = 'Commuter Rail' and operator = 'SEPTA'
        order by station)
    select * from joined_model_with_tod
     """


if __name__ == "__main__":

    for scenario in station_summary_files:
        existing_raw_table = scenario.sql_tablename
        new_tablename = existing_raw_table.replace("public.", "computed.")
        query = query_template.replace(
            "TABLENAME_PLACEHOLDER", scenario.sql_tablename
        ).replace("NEW_TABLENAME", new_tablename)
        db.execute(query)
