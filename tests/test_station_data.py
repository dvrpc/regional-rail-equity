import pytest

from regional_rail_equity import db
from regional_rail_equity.database.config.station_summary_config import station_summary_files


@pytest.mark.parametrize(
    "tablename", ["building_on_our_strengths_stations", "model_rr_station_stoppoints"]
)
def test_spatial_tables(tablename):
    """
    Confirm that all spatial tables exist
    """

    assert f"public.{tablename}" in db.tables(spatial_only=True)


@pytest.mark.parametrize("tablename", [x.sql_tablename for x in station_summary_files])
def test_nonspatial_tables(tablename):
    """
    Confirm that all NON-spatial tables exist
    """

    assert tablename in db.tables()
