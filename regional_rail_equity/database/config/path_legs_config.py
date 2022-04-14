"""
This file contains the configurations necessary to import all '.att' files
for the path leg model outputs
"""

from sqlalchemy.types import String, Float

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

# the 2045 tables have the same columns as 2019, but don't include the final two (LINENAME & FARETW)
cols_2045 = cols_2019[:-2]

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

year2045am_nobuild = {
    "filename": "2045_NoBld_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.nobuild_2045am_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
}

year2045md_nobuild = {
    "filename": "2045_NoBld_MD_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.nobuild_2045md_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
}
year2045pm_nobuild = {
    "filename": "2045_NoBld_PM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.nobuild_2045pm_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
}
year2045nt_nobuild = {
    "filename": "2045_NoBld_NT_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
    "sql_tablename": "public.nobuild_2045nt_home_to_dest_zone_fullpath",
    "column_idx_with_no_zeros": 4,
    "column_names": cols_2045,
}


path_legs_config = [
    year2019am,
    # year2045am_nobuild,
    # year2045md_nobuild,
    # year2045pm_nobuild,
    # year2045nt_nobuild,
]


# OLD IMPORT SETTINGS:
# f1 = ATTFileImporter(
#     filename="2019_AM_from_home_only_Full_Path_RR_Station_to_Destination_Zone.att",
#     sql_tablename="public.existing_2019am_rr_to_dest_zone_fullpath",
#     column_names=[
#         "ORIGZONENO",
#         "DESTZONENO",
#         "PATHINDEX",
#         "PATHLEGINDEX",
#         "ODTRIPS",
#         "FROMSTOPPOINTNO",
#         "FROMSTOPAREANO",
#         "TOSTOPPOINTNO",
#         "TOSTOPAREANO",
#         "TIMEPROFILEKEYSTRING",
#         "TIME",
#         "WAITTIME",
#         "DIST",
#         "LINENAME",
#         "FARETW",
#     ],
#     column_idx_with_no_zeros=4,
# )
# f2 = ATTFileImporter(
#     filename="2019_AM_from_home_only_Transit_Path_RR_Station_to_Stop_Point.att",
#     sql_tablename="public.existing_2019am_rr_to_stop_point_transitpath",
#     column_names=[
#         "ORIGZONENO",
#         "DESTZONENO",
#         "PATHINDEX",
#         "PATHLEGINDEX",
#         "ODTRIPS",
#         "FROMSTOPPOINTNO",
#         "FROMSTOPAREANO",
#         "TOSTOPPOINTNO",
#         "TOSTOPAREANO",
#         "TIMEPROFILEKEYSTRING",
#         "TIME",
#         "WAITTIME",
#         "DIST",
#         "LINENAME",
#         "FARETW",
#     ],
#     column_idx_with_no_zeros=4,
# )
# f3 = ATTFileImporter(
#     filename="2019_AM_from_home_only_Matrix2150_TrAuto_Home_to_Destination_Zone.att",
#     sql_tablename="public.existing_2019am_home_to_dest_2150",
#     column_names=[
#         "FROMZONENO",
#         "TOZONENO",
#         "MATVALUE2150",
#     ],
#     column_idx_with_no_zeros=2,
#     dtypes={
#         "fromzoneno": String(),
#         "tozoneno": String(),
#         "matvalue2150": Float(),
#     },
# )
# f4 = ATTFileImporter(
#     filename="2019_AM_from_home_only_Matrix2152_TrAuto_Home_to_Station_Person_Trips.att",
#     sql_tablename="public.existing_2019am_home_to_station_2152",
#     column_names=[
#         "FROMZONENO",
#         "TOZONENO",
#         "MATVALUE2152",
#     ],
#     column_idx_with_no_zeros=2,
#     dtypes={
#         "fromzoneno": String(),
#         "tozoneno": String(),
#         "matvalue2152": Float(),
#     },
# )
# f5 = ATTFileImporter(
#     filename="2019_AM_from_home_only_Matrix2200_TrTotal_Home_to_Destination_Zone.att",
#     sql_tablename="public.existing_2019am_home_to_dest_2200",
#     column_names=[
#         "FROMZONENO",
#         "TOZONENO",
#         "MATVALUE2200",
#     ],
#     column_idx_with_no_zeros=2,
#     dtypes={
#         "fromzoneno": String(),
#         "tozoneno": String(),
#         "matvalue2200": Float(),
#     },
# )
