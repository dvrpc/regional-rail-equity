from dataclasses import dataclass
from os import path
from pathlib import Path
from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER
from regional_rail_equity.helpers import print_title, print_msg

EXISTING_PATH_LEG_FILE = GDRIVE_PROJECT_FOLDER / "Data/Inputs/PathLegs/PUTPATHLEG.csv"


@dataclass
class PathLegImport:
    filepath: Path
    tablename: str


PATH_FILES = [
    PathLegImport(
        filepath=EXISTING_PATH_LEG_FILE,
        tablename="data.existing_path_legs",
    )
]


@print_title("IMPORTING PATH LEG TEXT FILE FROM GDRIVE")
def import_path_leg_file(db: Database) -> None:

    for pathfile in PATH_FILES:
        if pathfile.tablename not in db.tables():

            print_msg(f"Importing table: '{pathfile.tablename}'")

            db.import_file_with_pandas(
                filepath=pathfile.filepath,
                tablename=pathfile.tablename,
            )
        else:
            print_msg(
                f"The table '{pathfile.tablename}' already exists in this database. Skipping.",
                bullet="~~",
            )


if __name__ == "__main__":
    import_path_leg_file(db)
