from pathlib import Path
import geopandas as gpd
from dataclasses import dataclass
from pathlib import Path
from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER
from regional_rail_equity.helpers import print_title, print_msg

TAZ_SHAPEFILE = GDRIVE_PROJECT_FOLDER / "Data/Inputs/Zonal Data" / "2010_TAZ.shp"
TIM_ZONE_SHAPEFILE = GDRIVE_PROJECT_FOLDER / "Data/Inputs/PathLegs" / "TIM_24__zone.SHP"


@dataclass
class ShapefileToImport:
    filepath: Path
    sql_tablename: str
    explode: bool
    gpd_kwargs: dict


shapefiles = [
    ShapefileToImport(
        filepath=TAZ_SHAPEFILE,
        sql_tablename="data.taz_2010",
        explode=True,
        gpd_kwargs={"if_exists": "replace"},
    ),
    ShapefileToImport(
        filepath=TIM_ZONE_SHAPEFILE,
        sql_tablename="data.tim24_zones",
        explode=True,
        gpd_kwargs={"if_exists": "replace"},
    ),
]


@print_title("IMPORTING SPATIAL ZONE TABLE FROM SHAPEFILE ON GDRIVE")
def import_zone_shapes(db: Database, shapefiles: list[ShapefileToImport] = shapefiles) -> None:
    """
    Import the 2010 TAZ shapefiles into PostGIS

    Arguments:
        db (Database): analysis database
        filepath (Path): full path to the shapefile

    Returns:
        None: but creates a new spatial table in the database
    """

    for shp in shapefiles:
        if shp.sql_tablename not in db.tables(spatial_only=True):
            print_msg(f"Importing '{shp.sql_tablename}'")
            db.import_gis(
                filepath=shp.filepath,
                sql_tablename=shp.sql_tablename,
                explode=shp.explode,
                gpd_kwargs=shp.gpd_kwargs,
            )
        else:
            print_msg(
                f"The table '{shp.sql_tablename}' already exists in this database. Skipping.",
                bullet="~~",
            )


@print_title("IMPORTING SPATIAL TABLES FROM OPEN DATA PORTALS")
def import_geojsons(db: Database) -> None:
    """
    Import geojson data

    From SEPTA's open data portal:
        - Lines: https://septaopendata-septa.opendata.arcgis.com/datasets/SEPTA::septa-regional-rail-lines/about
        - Stations: https://septaopendata-septa.opendata.arcgis.com/datasets/SEPTA::septa-regional-rail-stations/about

    From DVRPC's open data portal:
        - Counties: https://dvrpc-dvrpcgis.opendata.arcgis.com/datasets/dvrpcgis::greater-philadelphia-region-county-boundaries-polygon/about
    """

    datasets = [
        {
            "sql_tablename": "data.regional_rail_lines",
            "filepath": "https://opendata.arcgis.com/datasets/48b0b600abaa4ca1a1bacf917a31c29a_0.geojson",
        },
        {
            "sql_tablename": "data.regional_rail_stations",
            "filepath": "https://opendata.arcgis.com/datasets/64eaa4539cf4429095c2c7bf25c629a2_0.geojson",
        },
        {
            "sql_tablename": "data.dvrpc_all_counties",
            "filepath": "https://arcgis.dvrpc.org/portal/rest/services/Boundaries/CountyBoundaries/FeatureServer/0/query?where=1=1&outfields=*&outsr=4326&f=geojson",
        },
    ]

    tables_currently_in_database = db.tables(spatial_only=True)

    for dataset in datasets:
        if f"{dataset['sql_tablename']}" not in tables_currently_in_database:
            print_msg(f"Importing '{dataset['sql_tablename']}'")
            gdf = gpd.read_file(dataset["filepath"])
            gdf.to_crs(epsg=26918, inplace=True)
            db.import_geodataframe(
                gdf,
                tablename=dataset["sql_tablename"],
                explode=True,
                gpd_kwargs={"index": False},
            )
        else:
            print_msg(
                f"The table '{dataset['sql_tablename']}' already exists in this database. Skipping.",
                bullet="~~",
            )


if __name__ == "__main__":
    import_geojsons(db)
    import_zone_shapes(db)
