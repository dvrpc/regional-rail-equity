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

year2019md = {
    "filename": "RE_2019_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.existing_2019md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2019,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "existing_2019md",
}


year2019pm = {
    "filename": "RE_2019_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.existing_2019pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2019,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "existing_2019pm",
}


year2019nt = {
    "filename": "RE_2019_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.existing_2019nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2019,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "existing_2019nt",
}


# Scenario 1 -------------------------------------------------------------------------------------------

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

# Scenario 2 -------------------------------------------------------------------------------------------

year2045s2am = {
    "filename": "2045_Scenario2_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario2_2045am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario2_2045am",
}

year2045s2md = {
    "filename": "2045_Scenario2_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario2_2045md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario2_2045md",
}

year2045s2pm = {
    "filename": "2045_Scenario2_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario2_2045pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario2_2045pm",
}

year2045s2nt = {
    "filename": "2045_Scenario2_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario2_2045nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario2_2045nt",
}

# Scenario 3 -------------------------------------------------------------------------------------------

year2045s3am = {
    "filename": "2045_Scenario3_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3_2045am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3_2045am",
}

year2045s3md = {
    "filename": "2045_Scenario3_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3_2045md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3_2045md",
}

year2045s3pm = {
    "filename": "2045_Scenario3_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3_2045pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3_2045pm",
}

year2045s3nt = {
    "filename": "2045_Scenario3_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3_2045nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3_2045nt",
}
# Scenario 3a (redo of s3))--------------------------------------------------------------------------------

year2045s3_a_am = {
    "filename": "2045_Scenario3a_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3a_2045am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3a_2045am",
}

year2045s3_a_md = {
    "filename": "2045_Scenario3a_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3a_2045md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3a_2045md",
}

year2045s3_a_pm = {
    "filename": "2045_Scenario3a_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3a_2045pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3a_2045pm",
}

year2045s3_a_nt = {
    "filename": "Re_2045_Scenario3a_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.scenario3a_2045nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
    "dtypes": {
        "origzoneno": String(),
        "odtrips": Float(),
        "minutes": Float(),
        "faretw": Float(),
    },
    "summary_tabname": "scenario3a_2045nt",
}


path_legs_config = [
    year2019am,
    year2019md,
    year2019nt,
    year2019pm,
    year2045s1am,
    year2045s1md,
    year2045s1pm,
    year2045s1nt,
    year2045s2am,
    year2045s2md,
    year2045s2pm,
    year2045s2nt,
    year2045s3am,
    year2045s3md,
    year2045s3pm,
    year2045s3nt,
    year2045s3_a_am,
    year2045s3_a_md,
    year2045s3_a_pm,
    year2045s3_a_nt,
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
mat2152_year2019md = {
    "filename": "2019_MD_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.existing_2019md_home_to_station_2152",
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
mat2152_year2019pm = {
    "filename": "2019_PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.existing_2019pm_home_to_station_2152",
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
mat2152_year2019nt = {
    "filename": "2019_NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.existing_2019nt_home_to_station_2152",
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

# Scenario 1 PNR
# ---------------------------------------

mat2152_year2045s1am = {
    "filename": "2045_Scenario1_ AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
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
    "filename": "2045_Scenario1_ PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
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
    "filename": "2045_Scenario1_ NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
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

# Scenario 2 PNR
# ---------------------------------------

mat2152_year2045s2am = {
    "filename": "2045_Scenario2_ AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario2_2045am_home_to_station_2152",
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

mat2152_year2045s2md = {
    "filename": "2045_Scenario2_ MD_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario2_2045md_home_to_station_2152",
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

mat2152_year2045s2pm = {
    "filename": "2045_Scenario2_ PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario2_2045pm_home_to_station_2152",
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

mat2152_year2045s2nt = {
    "filename": "2045_Scenario2_ NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario2_2045nt_home_to_station_2152",
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

# Scenario 3 PNR
# ---------------------------------------

mat2152_year2045s3am = {
    "filename": "2045_Scenario3_ AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3_2045am_home_to_station_2152",
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

mat2152_year2045s3md = {
    "filename": "2045_Scenario3_ MD_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3_2045md_home_to_station_2152",
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

mat2152_year2045s3pm = {
    "filename": "2045_Scenario3_ PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3_2045pm_home_to_station_2152",
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

mat2152_year2045s3nt = {
    "filename": "2045_Scenario3_ NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3_2045nt_home_to_station_2152",
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

# Scenario 3a PNR (redo of s3)
# ---------------------------------------

mat2152_year2045s3_a_am = {
    "filename": "2045_Scenario3a_AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3a_2045am_home_to_station_2152",
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

mat2152_year2045s3_a_md = {
    "filename": "2045_Scenario3a_MD_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3a_2045md_home_to_station_2152",
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

mat2152_year2045s3_a_pm = {
    "filename": "2045_Scenario3a_PM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3a_2045pm_home_to_station_2152",
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

mat2152_year2045s3_a_nt = {
    "filename": "2045_Scenario3a_NT_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
    "sql_tablename": "public.scenario3a_2045nt_home_to_station_2152",
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
    mat2152_year2019md,
    mat2152_year2019pm,
    mat2152_year2019nt,
    mat2152_year2045s1am,
    mat2152_year2045s1md,
    mat2152_year2045s1pm,
    mat2152_year2045s1nt,
    mat2152_year2045s2am,
    mat2152_year2045s2md,
    mat2152_year2045s2pm,
    mat2152_year2045s2nt,
    mat2152_year2045s3am,
    mat2152_year2045s3md,
    mat2152_year2045s3pm,
    mat2152_year2045s3nt,
    mat2152_year2045s3_a_am,
    mat2152_year2045s3_a_md,
    mat2152_year2045s3_a_pm,
    mat2152_year2045s3_a_nt,
]
