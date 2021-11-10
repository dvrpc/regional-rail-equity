from pathlib import Path
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
    db.import_gis(
        filepath=filepath,
        sql_tablename="taz_2010",
        explode=True,
        gpd_kwargs={"if_exists": "replace"},
    )


if __name__ == "__main__":
    import_zone_shapes(db)
