import pytest

from regional_rail_equity import db
from regional_rail_equity.database.config.path_legs_config import path_legs_config


@pytest.mark.parametrize("tablename", [config["sql_tablename"] for config in path_legs_config])
def test_table_import(tablename):
    """
    Confirm that all of the model files exist in the database
    """

    assert tablename in db.tables()
