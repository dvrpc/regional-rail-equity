import pytest

from regional_rail_equity import db

ALL_TABLES = [
    "ctpp_travel_mode",
    "ctpp_language_at_home",
    "ctpp_race_all_people",
    "ctpp_poverty_by_household",
    "regional_rail_lines",
    "regional_rail_stations",
    "taz_2010",
    "existing_2019_am_hwy_transit_od",
    "existing_2019_md_hwy_transit_od",
    "existing_2019_pm_hwy_transit_od",
    "existing_2019_nt_hwy_transit_od",
]


@pytest.mark.parametrize("tablename", ALL_TABLES)
def test_table_import(tablename):

    assert f"public.{tablename}" in db.tables()


def test_spatial_table_projections():
    for tablename, epsg in db.query("select f_table_name, srid from geometry_columns;"):
        assert epsg == 26918, f"{tablename} has the wrong projection"
