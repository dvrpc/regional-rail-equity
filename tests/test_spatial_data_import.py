import pytest

from regional_rail_equity import db

ALL_TABLES = [
    "data.regional_rail_lines",
    "data.regional_rail_stations",
    "data.dvrpc_counties",
    "data.dvrpc_all_counties",
    "data.taz_2010",
    "data.tim24_zones",
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
