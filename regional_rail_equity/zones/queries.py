from dataclasses import dataclass


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

    def name_sql(self) -> str:
        txt = self.name.lower()
        for char in [" ", "-", "(", ")"]:
            txt = txt.replace(char, "_")
        return txt

    def compute_table(self, scenario_name: str, timeframe: str, directionality: str = "to") -> None:
        query_templates = {"to": zone_as_destination, "from": zone_as_origin}

        query_content = (
            query_templates[directionality]
            .replace("NAME_OF_ZONE", self.name)
            .replace("SCENARIO", scenario_name)
            .replace("TIMEFRAME", timeframe)
        )

        query = f"""
            create table if not exists
                computed.{scenario_name}_{timeframe}_{directionality}_{self.name_sql()}
            as (
                {query_content}
            )
        """
        self.db.execute(query)
