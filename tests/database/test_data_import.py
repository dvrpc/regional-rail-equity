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
    "public.existing_2019am_rr_to_dest_zone_fullpath",
    "public.existing_2019am_rr_to_stop_point_transitpath",
    "public.existing_2019am_home_to_dest_2150",
    "public.existing_2019am_home_to_station_2152",
    "public.existing_2019am_home_to_dest_2200",
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
