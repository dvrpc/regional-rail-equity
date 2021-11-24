from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_title

ALL_SCHEMAS = ["computed"]


@print_title("CREATING NEW SCHEMAS")
def create_schemas(db: Database) -> None:
    """
    Create schemas that will be needed later

    Arguments:
        db (Database): analysis database
    """

    for schema in ALL_SCHEMAS:
        db.schema_add(schema)


if __name__ == "__main__":
    create_schemas(db)
