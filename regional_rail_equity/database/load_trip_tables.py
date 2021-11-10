from pathlib import Path
import pandas as pd
from sqlalchemy.types import Float, String
from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER


def find_header_row_index(data_list: list) -> int:
    """
    Model outputs have roughly 12 rows of front-matter before the data starts.

    This function finds the row index of the actual header,
    which looks like this:
        $ODPAIR:FROMZONENO	TOZONENO	MATVALUE(2000)	MATVALUE(2200)

    Arguments:
        data_list (list): data from text file that has been read into memory

    Returns:
        int: the index of the true header row
    """
    for index, row in enumerate(data_list):
        if "$ODPAIR" in row:
            return index


def load_single_trip_table(filepath: Path) -> pd.DataFrame:
    """
    For a given O/D file:
        - read the data
        - transform tab-delimited strings into list
        - drop rows with no trips
        - load into a pandas dataframe

    Arguments:
        filepath (Path): a single path to a single file

    Returns:
        pd.DataFrame: with all non-empty rows from the text file
    """
    # read the text file into a list
    with open(filepath, "r", newline="\r\n") as openfile:
        data_with_headers = openfile.readlines()

    # remove the header rows, and split tab-delimited text into list
    index_slice = find_header_row_index(data_with_headers) + 1
    data = [row.replace("\r\n", "").split("\t") for row in data_with_headers[index_slice:]]

    # drop rows that have zeros in both "MATVALUE" fields
    # FROMZONENO	TOZONENO	MATVALUE(2000)	MATVALUE(2200)
    data_without_nulls = [
        row for row in data if len(row) == 4 and (float(row[2]) > 0 or float(row[3]) > 0)
    ]

    # load into pandas dataframe
    df = pd.DataFrame(data_without_nulls, columns=["fromzone", "tozone", "mat2000", "mat2200"])
    return df


def load_trip_tables(
    db: Database, table_prefix: str = "existing", subfolder: str = "Trip Tables"
) -> None:
    """
    Load all trip tables within a given subfolder.
    All '*.att' tables in the folder will be imported with the table_prefix.

    Arguments:
        db (Database): postgresql database for the analysis
        table_prefix (str): the value that will appear before each tablename
        subfolder (str): the folder under GDRIVE_PROJECT_FOLDER that has the files

    Returns:
        None: but creates a new postgresql table for each text file

    """
    trip_table_folder = GDRIVE_PROJECT_FOLDER / subfolder

    files_to_import = trip_table_folder.rglob("*.att")

    for trip_file in files_to_import:
        sql_tablename = f"{table_prefix}_{trip_file.stem.lower()}"

        df = load_single_trip_table(trip_file)

        print("Importing", trip_file.stem)

        db.import_dataframe(
            df,
            sql_tablename,
            df_import_kwargs={
                "if_exists": "replace",
                "index": False,
                "dtype": {
                    "fromzone": String(),
                    "tozone": String(),
                    "mat2000": Float(),
                    "mat2200": Float(),
                },
            },
        )


if __name__ == "__main__":
    load_trip_tables(db)
