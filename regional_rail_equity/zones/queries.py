from dataclasses import dataclass
from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_msg, print_title

zone_as_destination = f"""
    with zones_shapes as (
        select tazt, geom
        from taz_2010 
        order by tazt
    ),
    origins as (
        select
            od.fromzone,
            sum(od.mat2000) as mat2000sum,
            sum(od.mat2200) as mat2200sum
        from
            SCENARIO_TIMEFRAME_hwy_transit_od od
        where od.tozone in (
            select tazt from zones
            where zone_name = 'NAME_OF_ZONE'
        )
        group by od.fromzone
    )
    
    select
        z.tazt, z.geom,
        o.fromzone, o.mat2000sum, o.mat2200sum
    
    from zones_shapes z
    inner join origins o
    on z.tazt = o.fromzone
"""

zone_as_origin = f"""
    with zones_shapes as (
        select tazt, geom
        from taz_2010 
        order by tazt
    ),
    destinations as (
        select
            od.tozone,
            sum(od.mat2000) as mat2000sum,
            sum(od.mat2200) as mat2200sum
        from
            SCENARIO_TIMEFRAME_hwy_transit_od od
        where od.fromzone in (
            select tazt from zones
            where zone_name = 'NAME_OF_ZONE'
        )
        group by od.tozone
    )
    
    select
        z.tazt, z.geom,
        d.tozone, d.mat2000sum, d.mat2200sum
    
    from zones_shapes z
    inner join destinations d
    on z.tazt = d.tozone
"""


@dataclass
class Zone:

    name: str
    db: Database

    def name_sql(self) -> str:
        txt = self.name.lower()
        for char in [" ", "-", "(", ")"]:
            txt = txt.replace(char, "_")
        return txt

    def compute(self, scenario_name: str, timeframe: str, directionality: str = "to") -> None:

        new_tablename = f"computed.{scenario_name}_{timeframe}_{directionality}_{self.name_sql()}"

        if new_tablename in self.db.tables():
            print_msg(f"This table already exists: '{new_tablename}'", bullet="~~")

        else:
            print_msg(f"Computing new table: '{new_tablename}'")

            query_templates = {"to": zone_as_destination, "from": zone_as_origin}

            query_content = (
                query_templates[directionality]
                .replace("NAME_OF_ZONE", self.name)
                .replace("SCENARIO", scenario_name)
                .replace("TIMEFRAME", timeframe)
            )

            query = f"create table {new_tablename} as ({query_content})"
            self.db.execute(query)


@print_title("COMPUTING ALL COMBINATIONS OF ZONES/SCENARIOS/TIMES/DIRECTIONS")
def compute_all_combinations(db: Database):

    all_zone_names = db.query_as_list_of_singletons("select distinct zone_name from zones")

    for zone_name in all_zone_names:
        zone = Zone(zone_name, db)
        for timeframe in ["am", "md", "pm", "nt"]:
            for directionality in ["to", "from"]:
                for scenario in ["existing_2019"]:
                    zone.compute(scenario, timeframe, directionality)


if __name__ == "__main__":
    compute_all_combinations(db)
