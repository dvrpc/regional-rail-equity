from regional_rail_equity import db
from regional_rail_equity.zones import zones

if __name__ == "__main__":
    query = f"""
    with zones as (
        select
            tazt,
            geom
        from
            taz_2010 
        order by
            tazt
    ),
    origins as (
        select
            fromzone,
            sum(mat2000) as mat2000sum,
            sum(mat2200) as mat2200sum
        from
            existing_2019_am_hwy_transit_od 
        where tozone::int in {zones.center_city_full.ids}
        group by fromzone
    )

    select
        z.tazt, z.geom,
        o.fromzone, o.mat2000sum, o.mat2200sum
    from
        zones z
    inner join
        origins o
    on
        z.tazt = o.fromzone
    """

    db.gis_make_geotable_from_query(query, "trips_into_center_city_am", "POLYGON", 26918)
