from regional_rail_equity import db
from regional_rail_equity.database.config.env_vars import GDRIVE_PROJECT_FOLDER
from regional_rail_equity.database.config.station_summary_config import station_summary_files
from regional_rail_equity.helpers import print_title, print_msg

TOD_FOLDER = GDRIVE_PROJECT_FOLDER / "Data/Inputs/TOD Station Summaries"


@print_title("Importing station GIS data from 'Building on our Strengths' project")
def import_gis():
    """
    Import the shapefile containing TOD analysis results
    for the Philly area rail stations from the
    'Building on our Strengths' report
    """
    db.import_gis(
        filepath=TOD_FOLDER / "TOD_Opportunities/TOD_Opportunities.shp",
        sql_tablename="building_on_our_strengths_stations",
        gpd_kwargs={"if_exists": "replace"},
    )

    db.import_gis(
        filepath=TOD_FOLDER
        / "Regional_Rail_Stations_stoppoint/Regional_Rail_Stations_stoppoint.SHP",
        sql_tablename="model_rr_station_stoppoints",
        gpd_kwargs={"if_exists": "replace"},
    )


@print_title("Importing station-level summary files")
def import_excel():
    """
    Import all of the configured Excel files with station-level summaries
    """
    for stationfile in station_summary_files:
        print_msg(f"Importing {stationfile.filename}")

        db.import_file_with_pandas(
            filepath=TOD_FOLDER / stationfile.filename,
            tablename=stationfile.sql_tablename,
            pd_read_kwargs={"skiprows": stationfile.skiprows},
            df_import_kwargs={"if_exists": "replace"},
        )


if __name__ == "__main__":
    import_gis()
    import_excel()
