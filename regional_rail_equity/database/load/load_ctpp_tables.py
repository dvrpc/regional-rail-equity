"""
load_ctpp_tables.py
-------------------


"""
from __future__ import annotations, print_function
import geopandas as gpd
from dataclasses import dataclass
from pg_data_etl import Database
from pg_data_etl.database.actions.import_geo_data import import_geodataframe

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER

from regional_rail_equity.database.config.ctpp_config import ctpp_configurations
from regional_rail_equity.helpers import print_title, print_msg

CTPP_FOLDER = GDRIVE_PROJECT_FOLDER / "Data" / "Inputs" / "CTPP-equity"


@dataclass
class CTPPFile:
    """
    `CTPPFile` is a class that:
        - loads a TAZ shapefile downloaded from the CTPP website
        - swaps in human-readable column names
        - drops TAZs outside the PA-side of the DVRPC region

    https://ctpp.transportation.org/ctpp-data-set-information/
    """

    filepath: str
    sql_tablename: str
    names: list[str]
    gdf: gpd.GeoDataFrame | None = None

    def load(self):
        """
        - Read the shapefile
        - convert EPSG to 26918
        - update column names
        - drop TAZs outside region
        """
        self.gdf = gpd.read_file(CTPP_FOLDER / self.filepath)
        self.gdf.to_crs(epsg=26918, inplace=True)
        self.gdf.columns = self.names
        self.filter_gdf_to_region()

    def filter_gdf_to_region(self):
        """
        Filter the geodataframe to only contain counties in the DVRPC region
        """
        counties = {
            "Philadelphia": "Pennsylvania",
            "Bucks": "Pennsylvania",
            "Chester": "Pennsylvania",
            "Montgomery": "Pennsylvania",
            "Delaware": "Pennsylvania",
            "Mercer": "New Jersey",
            "Burlington": "New Jersey",
            "Gloucester": "New Jersey",
            "Camden": "New Jersey",
        }
        self.gdf = self.gdf[
            self.gdf["name"].str.contains(
                "|".join([f"{x} County, {counties.get(x)}" for x in counties])
            )
        ]

    def import_to_database(self, db: Database):
        """
        Load the shapefile and import it into PostGIS
        """

        if self.sql_tablename not in db.tables():
            print_msg(f"Importing {self.sql_tablename}")

            self.load()
            db.import_geodataframe(self.gdf, self.sql_tablename)
        else:
            print_msg(
                f"The table '{self.sql_tablename}' already exists. Skipping.",
                bullet="~~",
            )


@print_title("IMPORTING CTPP TABLES WITH EQUITY DATA")
def import_ctpp_tables(db: Database) -> None:
    """
    Import CTPP shapefiles:
        - EA_A113100 - Poverty status
        - EA_A101105 - Minority Status
        - EA_A117200 - Ability to speak English by Language spoken at home
    """

    for kwargs in ctpp_configurations:
        ctpp_file = CTPPFile(**kwargs)
        ctpp_file.import_to_database(db)


if __name__ == "__main__":
    import_ctpp_tables(db)
