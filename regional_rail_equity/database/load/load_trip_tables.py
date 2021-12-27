from __future__ import annotations
from pathlib import Path
import pandas as pd
from sqlalchemy.types import Float, String
from dataclasses import dataclass
from pg_data_etl import Database

from regional_rail_equity import db, GDRIVE_PROJECT_FOLDER
from regional_rail_equity.helpers import print_title, print_msg


def find_header_row_index(data_list: list) -> int:
    """
    Model outputs have roughly 12 rows of front-matter before the data starts.

    This function finds the row index of the actual header,
    which looks like this:
        $ODPAIR:FROMZONENO	TOZONENO	MATVALUE(2000)	MATVALUE(2200)
    or this:
        $PUTPATHLEG:ORIGZONENO	DESTZONENO	PATHINDEX	PATHLEGINDEX	ODTRIPS	FROMSTOPPOINTNO	FROMSTOPAREANO	TOSTOPPOINTNO	TOSTOPAREANO	TIMEPROFILEKEYSTRING	TIME	WAITTIME	DIST	LINENAME	FARE(TW)

    Arguments:
        data_list (list): data from text file that has been read into memory

    Returns:
        int: the index of the true header row
    """
    for index, row in enumerate(data_list):
        if "$ODPAIR" in row or "$PUTPATHLEG" in row:
            return index


def load_single_trip_table(
    filepath: Path, column_names: list, column_idx_with_no_zeros: int = 2
) -> pd.DataFrame:
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
        row
        for row in data
        if len(row) == len(column_names) and float(row[column_idx_with_no_zeros]) > 0
    ]

    # load into pandas dataframe
    df = pd.DataFrame(data_without_nulls, columns=column_names)
    return df


@dataclass
class ATTFileImporter:
    filename: str
    column_names: list
    sql_tablename: str
    dtypes: dict = None
    column_idx_with_no_zeros: int = 2

    @property
    def filepath(self):
        return (
            GDRIVE_PROJECT_FOLDER / "Data/Inputs/Model Exports for Equity Analysis" / self.filename
        )

    @property
    def lowercase_columns(self):
        return [x.lower() for x in self.column_names]


def import_single_table(db: Database, file_to_import: ATTFileImporter) -> None:
    """

    Arguments:
        db (Database): postgresql database for the analysis
        table_prefix (str): the value that will appear before each tablename
        subfolder (str): the folder under GDRIVE_PROJECT_FOLDER that has the files
        glob_string (str): the regex used by pathlib to find matching filenames

    Returns:
        None: but creates a new postgresql table for each text file

    """
    existing_tables = db.tables()

    if file_to_import.sql_tablename not in existing_tables:
        df = load_single_trip_table(
            file_to_import.filepath,
            file_to_import.lowercase_columns,
            file_to_import.column_idx_with_no_zeros,
        )

        print_msg(f"Importing {file_to_import.filepath.stem}")

        import_kwargs = {"index": False}

        if file_to_import.dtypes:
            import_kwargs["dtype"] = file_to_import.dtypes

        db.import_dataframe(
            df,
            file_to_import.sql_tablename,
            df_import_kwargs=import_kwargs,
        )
    else:

        print_msg(
            f"The table '{file_to_import.sql_tablename}' already exists in this database. Skipping.",
            bullet="~~",
        )


@print_title("IMPORTING ORIGIN/DESTINATION TABLES FROM TEXT FILES ON GDRIVE")
def load_trip_tables(db: Database) -> None:

    f1 = ATTFileImporter(
        filename="2019_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
        sql_tablename="public.existing_2019am_rr_to_dest_zone_fullpath",
        column_names=[
            "ORIGZONENO",
            "DESTZONENO",
            "PATHINDEX",
            "PATHLEGINDEX",
            "ODTRIPS",
            "FROMSTOPPOINTNO",
            "FROMSTOPAREANO",
            "TOSTOPPOINTNO",
            "TOSTOPAREANO",
            "TIMEPROFILEKEYSTRING",
            "TIME",
            "WAITTIME",
            "DIST",
            "LINENAME",
            "FARETW",
        ],
        column_idx_with_no_zeros=4,
    )
    f2 = ATTFileImporter(
        filename="2019_AM_from_home_only_Transit_Path_RR_Station_to_Stop_Point.att",
        sql_tablename="public.existing_2019am_rr_to_stop_point_transitpath",
        column_names=[
            "ORIGZONENO",
            "DESTZONENO",
            "PATHINDEX",
            "PATHLEGINDEX",
            "ODTRIPS",
            "FROMSTOPPOINTNO",
            "FROMSTOPAREANO",
            "TOSTOPPOINTNO",
            "TOSTOPAREANO",
            "TIMEPROFILEKEYSTRING",
            "TIME",
            "WAITTIME",
            "DIST",
            "LINENAME",
            "FARETW",
        ],
        column_idx_with_no_zeros=4,
    )
    f3 = ATTFileImporter(
        filename="2019_AM_from_home_only_Matrix2150_TrAuto_Home_to_Destination_Zone.att",
        sql_tablename="public.existing_2019am_home_to_dest_2150",
        column_names=[
            "FROMZONENO",
            "TOZONENO",
            "MATVALUE2150",
        ],
        column_idx_with_no_zeros=2,
        dtypes={
            "fromzoneno": String(),
            "tozoneno": String(),
            "matvalue2150": Float(),
        },
    )
    f4 = ATTFileImporter(
        filename="2019_AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
        sql_tablename="public.existing_2019am_home_to_station_2152",
        column_names=[
            "FROMZONENO",
            "TOZONENO",
            "MATVALUE2152",
        ],
        column_idx_with_no_zeros=2,
        dtypes={
            "fromzoneno": String(),
            "tozoneno": String(),
            "matvalue2152": Float(),
        },
    )
    f5 = ATTFileImporter(
        filename="2019_AM_from_home_only_Matrix2200_TrTotal_Home_to_Destination_Zone.att",
        sql_tablename="public.existing_2019am_home_to_dest_2200",
        column_names=[
            "FROMZONENO",
            "TOZONENO",
            "MATVALUE2200",
        ],
        column_idx_with_no_zeros=2,
        dtypes={
            "fromzoneno": String(),
            "tozoneno": String(),
            "matvalue2200": Float(),
        },
    )

    for file_to_import in [f1, f2, f3, f4, f5]:
        import_single_table(db, file_to_import)


if __name__ == "__main__":
    load_trip_tables(db)
