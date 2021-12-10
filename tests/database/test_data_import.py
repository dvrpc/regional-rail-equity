import pytest

from regional_rail_equity import db

ALL_TABLES = [
    "data.ctpp_travel_mode",
    "data.ctpp_language_at_home",
    "data.ctpp_race_all_people",
    "data.ctpp_poverty_by_household",
    "data.regional_rail_lines",
    "data.regional_rail_stations",
    "data.dvrpc_counties",
    "data.dvrpc_pa_counties",
    "data.taz_2010",
    # "data.existing_2019_am_hwy_transit_od",
    # "data.existing_2019_md_hwy_transit_od",
    # "data.existing_2019_pm_hwy_transit_od",
    # "data.existing_2019_nt_hwy_transit_od",
    "data.existing_path_legs",
    "data.existing_od_transit_auto",
]


@pytest.mark.parametrize("tablename", ALL_TABLES)
def test_table_import(tablename):
    """
    Confirm that all of the necessary tables exist
    inside the database, within the `public` schema
    """

    assert tablename in db.tables()


def test_spatial_table_projections():
    """
    Confirm that all spatial tables have
    the proper projection: EPSG 26918
    """
    for tablename, epsg in db.query("select f_table_name, srid from geometry_columns"):
        assert epsg == 26918, f"{tablename} has the wrong projection"
