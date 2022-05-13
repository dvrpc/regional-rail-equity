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

cols_2045 = [
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

year2045s1am = {
    "filename": "2045_Scenario1_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario1_2045am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario1_2045am",
}

year2045s1md = {
    "filename": "2045_Scenario1_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario1_2045md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario1_2045md",
}

year2045s1pm = {
    "filename": "2045_Scenario1_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario1_2045pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario1_2045pm",
}

year2045s1nt = {
    "filename": "2045_Scenario1_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario1_2045nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario1_2045nt",
}


path_legs_config = [
    year2019am,
    year2045s1am,
    year2045s1md,
    year2045s1pm,
    year2045s1nt,
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

mat2152_year2045s1am = {
    "filename": "2045_Scenario1_AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario1_2045am_home_to_station_2152",
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

mat2152_year2045s1md = {
    "filename": "2045_Scenario1_MD_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario1_2045md_home_to_station_2152",
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

mat2152_year2045s1pm = {
    "filename": "2045_Scenario1_PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario1_2045pm_home_to_station_2152",
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

mat2152_year2045s1nt = {
    "filename": "2045_Scenario1_NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario1_2045nt_home_to_station_2152",
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
    mat2152_year2045s1am,
    mat2152_year2045s1md,
    mat2152_year2045s1pm,
    mat2152_year2045s1nt,
]
