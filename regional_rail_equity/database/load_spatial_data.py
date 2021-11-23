from pathlib import Path
import geopandas as gpd
from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER

TAZ_SHAPEFILE = GDRIVE_PROJECT_FOLDER / "Data/Inputs/Zonal Data" / "2010_TAZ.shp"


def import_zone_shapes(db: Database, filepath: Path = TAZ_SHAPEFILE) -> None:
    """
    Import the 2010 TAZ shapefile into PostGIS

    Arguments:
        db (Database): analysis database
        filepath (Path): full path to the shapefile

    Returns:
        None: but creates a new spatial table in the database
    """

    print("-----------------------------------------------------")
    print("IMPORTING SPATIAL ZONE TABLE FROM SHAPEFILE ON GDRIVE")

    if "public.taz_2010" not in db.tables(spatial_only=True):
        db.import_gis(
            filepath=filepath,
            sql_tablename="taz_2010",
            explode=True,
            gpd_kwargs={"if_exists": "replace"},
        )
    else:
        print(f"\t -> The table 'taz_2010' already exists in this database. Skipping.")


def import_septa_geojsons(db: Database) -> None:
    """
    Import geojson data for SEPTA regional rail:
        - Lines: https://septaopendata-septa.opendata.arcgis.com/datasets/SEPTA::septa-regional-rail-lines/about
        - Stations: https://septaopendata-septa.opendata.arcgis.com/datasets/SEPTA::septa-regional-rail-stations/about
    """

    print("------------------------------------------------------")
    print("IMPORTING SPATIAL TABLES FROM SEPTA'S OPEN DATA PORTAL")

    datasets = [
        {
            "sql_tablename": "regional_rail_lines",
            "filepath": "https://opendata.arcgis.com/datasets/48b0b600abaa4ca1a1bacf917a31c29a_0.geojson",
            "explode": True,
        },
        {
            "sql_tablename": "regional_rail_stations",
            "filepath": "https://opendata.arcgis.com/datasets/64eaa4539cf4429095c2c7bf25c629a2_0.geojson",
        },
    ]

    tables_currently_in_database = db.tables(spatial_only=True)

    for dataset in datasets:
        if f"public.{dataset['sql_tablename']}" not in tables_currently_in_database:
            print(f"\t -> Importing '{dataset['sql_tablename']}'")
            gdf = gpd.read_file(dataset["filepath"])
            gdf.to_crs(epsg=26918, inplace=True)
            db.import_geodataframe(
                gdf,
                tablename=dataset["sql_tablename"],
                explode=True,
                gpd_kwargs={"index": False},
            )
        else:
            print(
                f"\t -> The table '{dataset['sql_tablename']}' already exists in this database. Skipping."
            )


if __name__ == "__main__":
    import_septa_geojsons(db)
    import_zone_shapes(db)
