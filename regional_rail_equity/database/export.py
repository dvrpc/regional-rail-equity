from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER
from regional_rail_equity.helpers import print_title, print_msg

OUTPUT_SHP_FOLDER = GDRIVE_PROJECT_FOLDER / "Data" / "Outputs" / "GIS"

TABLES_TO_EXPORT = [
    "ctpp.summary",
    "regional_rail_lines",
    "regional_rail_stations",
]

QUERIES_TO_EXPORT = [
    {
        "filename": "trips_to_cc_existing_2019_am",
        "sql": """
            select *, st_area(geom) as area, mat2200sum / st_area(geom) as mat2200density
            from computed.existing_2019_am_to_center_city___girard_to_washington
            where st_within(st_centroid(geom), (select st_collect(geom) from public.dvrpc_pa_counties))
            """,
    },
    {
        "filename": "cc_zone_girard_to_washington",
        "sql": """
            select st_union(geom) as geom
            from taz_2010
            where tazt in (
                select tazt from zones
                where zone_name = 'Center City - Girard to Washington'
            )
            """,
    },
]


@print_title("EXPORTING SHAPEFILES FROM DATABASE")
def export_shapefiles(db: Database):
    for table in TABLES_TO_EXPORT:
        output_path = OUTPUT_SHP_FOLDER / (table.replace(".", "_") + ".shp")
        print_msg(f"Exporting: {table}")
        gdf = db.gdf(f"SELECT * FROM {table}")
        gdf.to_file(output_path)

    for table in QUERIES_TO_EXPORT:
        output_path = OUTPUT_SHP_FOLDER / (table["filename"] + ".shp")
        print_msg(f"Exporting: {table['filename']}")
        gdf = db.gdf(table["sql"])
        gdf.to_file(output_path)


if __name__ == "__main__":
    export_shapefiles(db)
