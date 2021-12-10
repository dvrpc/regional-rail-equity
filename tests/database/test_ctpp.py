import pytest

from regional_rail_equity import db


@pytest.mark.parametrize(
    "tablename",
    [
        "data.ctpp_travel_mode",
        "data.ctpp_language_at_home",
        "data.ctpp_race_all_people",
        "data.ctpp_poverty_by_household",
    ],
)
def test_number_of_tazs(tablename):
    """
    There are 2,182 traffic analysis zones
    within the five PA counties inside the
    DVRPC region. This test confirms
    that each table has all of the TAZs.
    """
    query = f"""
        select count(*) from {tablename}
    """

    assert db.query_as_singleton(query) == 2182
