import pytest

from regional_rail_equity import db
from regional_rail_equity.database.config.path_legs_config import path_legs_config, mat2152_config

imported_files = mat2152_config + path_legs_config


@pytest.mark.parametrize("tablename", [config["sql_tablename"] for config in imported_files])
def test_table_import(tablename):
    """
    Confirm that all of the model files exist in the database
    """

    assert tablename in db.tables()
