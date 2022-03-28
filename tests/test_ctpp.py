import pytest

from regional_rail_equity import db
from regional_rail_equity.database.config.ctpp_config import ctpp_configurations


@pytest.mark.parametrize(
    "tablename",
    [config["sql_tablename"] for config in ctpp_configurations] + ["ctpp.summary"],
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

    taz_counts = {"pa": 2182, "nj": 958, "all": 3140}

    result = db.query_as_singleton(query)
    if "nj" in tablename:
        expected_tazs = taz_counts["nj"]
    elif "pa" in tablename:
        expected_tazs = taz_counts["pa"]
    else:
        expected_tazs = taz_counts["all"]

    assert result == expected_tazs, f"{tablename} has the wrong number of tazs: {result}"
