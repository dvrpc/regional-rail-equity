"""
This file contains the configurations necessary to import all '.att' files
for the path leg model outputs
"""
from sqlalchemy.types import String, Float

# Path Legs Listing files
# -----------------------

cols_2019 = [
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
]


year2019am = {
    "filename": "2019_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.existing_2019am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2019,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "existing_2019am",
}


path_legs_config = [
    year2019am,
]

# Matrix 2152: Home TAZ to Park&Ride Zone
# ---------------------------------------

mat2152_year2019am = {
    "filename": "2019_AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.existing_2019am_home_to_station_2152",
    "column_names": [
        "FROMZONENO",
        "TOZONENO",
        "MATVALUE2152",
    ],
    "column_idx_with_no_zeros": 2,
    "dtypes": {
        "fromzoneno": String(),
        "tozoneno": String(),
        "matvalue2152": Float(),
    },
}

mat2152_config = [
    mat2152_year2019am,
]
