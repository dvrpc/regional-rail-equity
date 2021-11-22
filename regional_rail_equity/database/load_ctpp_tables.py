"""
load_ctpp_tables.py
-------------------


"""
from __future__ import annotations
import geopandas as gpd
from dataclasses import dataclass
from pg_data_etl import Database
from pg_data_etl.database.actions.import_geo_data import import_geodataframe

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER

CTPP_FOLDER = GDRIVE_PROJECT_FOLDER / "Data" / "Inputs" / "CTPP-equity"


@dataclass
class CTPPFile:
    """
    CTPPFile is a class that:
        - loads a TAZ shapefile downloaded from the CTPP website
        - swaps in human-readable column names
        - drops TAZs outside the PA-side of the DVRPC region
    """

    filepath: str
    sql_tablename: str
    names: list[str]
    gdf: gpd.GeoDataFrame | None = None

    def load(self):
        """Read the shapefile, convert to 26918, update column names, and drop TAZs outside region"""
        self.gdf = gpd.read_file(CTPP_FOLDER / self.filepath)
        self.gdf.to_crs(epsg=26918, inplace=True)
        self.gdf.columns = self.names
        self.filter_gdf_to_region()

    def filter_gdf_to_region(self):
        """Filter the geodataframe to only contain counties in the PA-side of the DVRPC region"""
        counties = ["Philadelphia", "Bucks", "Chester", "Montgomery", "Delaware"]
        self.gdf = self.gdf[
            self.gdf["name"].str.contains("|".join([f"{x} County" for x in counties]))
        ]

    def import_to_database(self, db: Database):
        """Load the shapefile and import it into PostGIS"""

        print(f"\t -> Importing {self.sql_tablename}")
        self.load()

        db.import_geodataframe(self.gdf, self.sql_tablename, gpd_kwargs={"if_exists": "replace"})


def import_ctpp_tables():

    print("--------------------------------------")
    print("IMPORTING CTPP TABLES WITH EQUITY DATA")

    files_to_import = [
        # POVERTY STATUS
        CTPPFile(
            filepath="EA_A113100 - Poverty status (4) (Households for which poverty status is determined)/C13.shp",
            sql_tablename="ctpp_poverty_by_household",
            names=[
                "ctpp_id",
                "label",
                "name",
                "geoid",
                "est_total_poverty_status",
                "moe_total_poverty_status",
                "est_below_100pct_poverty_status",
                "moe_below_100pct_poverty_status",
                "est_100_to_149pct_poverty_status",
                "moe_100_to_149pct_poverty_status",
                "est_at_or_above_150pct_poverty_status",
                "moe_at_or_above_150pct_poverty_status",
                "geometry",
            ],
        ),
        # RACE
        CTPPFile(
            filepath="EA_A101108 - Race (5) (All persons)/C13.shp",
            sql_tablename="ctpp_race_all_people",
            names=[
                "ctpp_id",
                "label",
                "name",
                "geoid",
                "est_all_races",
                "moe_all_races",
                "est_white_alone",
                "moe_white_alone",
                "est_black_alone",
                "moe_black_alone",
                "est_asian_alone",
                "moe_asian_alone",
                "est_other",
                "moe_other",
                "geometry",
            ],
        ),
    ]

    for ctppfile in files_to_import:
        ctppfile.import_to_database(db)


if __name__ == "__main__":
    import_ctpp_tables()
