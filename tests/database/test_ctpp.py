import pytest

from regional_rail_equity import db


@pytest.mark.parametrize(
    "tablename",
    [
        "ctpp_travel_mode",
        "ctpp_language_at_home",
        "ctpp_race_all_people",
        "ctpp_poverty_by_household",
    ],
)
def test_number_of_tazs(tablename):
    query = f"""
        select count(*) from {tablename}
    """

    assert db.query_as_singleton(query) == 2182
