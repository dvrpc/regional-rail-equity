from regional_rail_equity import db
from regional_rail_equity.database.config.path_legs_config import path_legs_config

query = """
    with joined_model_with_tod as(
        select *, st_transform(a.geom, 4326) from model_rr_station_stoppoints a
        right join building_on_our_strengths_stations b
        on st_dwithin(a.geom,b.geom,110)
        inner join station_summary_2045nobuild_am c 
        on a.no = c.stoppointno
        where b.type = 'Commuter Rail' and "operator" = 'SEPTA')
    select * from joined_model_with_tod
     """

if __name__ == "__main__":
    pass
