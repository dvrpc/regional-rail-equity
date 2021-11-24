import pytest

from regional_rail_equity import db

from regional_rail_equity.database.feature_engineering import ALL_SCHEMAS


@pytest.mark.parametrize("schema", ALL_SCHEMAS)
def test_schemas(schema):
    """
    Confirm that all necessary schemas exist
    """

    assert schema in db.schemas()
