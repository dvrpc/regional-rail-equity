from dataclasses import dataclass


@dataclass
class StationSummaryFile:
    filename: str
    skiprows: int
    sheetname: str
    sql_tablename: str


nobuild_2045_am = StationSummaryFile(
    filename="2045_NoBld_AM_from_home_only_Trip_Stats_by_Station.xlsx",
    skiprows=4,
    sheetname="Sheet1",
    sql_tablename="public.station_summary_2045nobuild_am",
)

# ----------Scenario 1 ----------------------------------------------------------
s1_am = StationSummaryFile(
    filename="RE_2045_Scenario1_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="AM",
    sql_tablename="public.station_summary_2045s1_am",
)
s1_md = StationSummaryFile(
    filename="RE_2045_Scenario1_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="MD",
    sql_tablename="public.station_summary_2045s1_md",
)
s1_pm = StationSummaryFile(
    filename="RE_2045_Scenario1_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="PM",
    sql_tablename="public.station_summary_2045s1_pm",
)
s1_nt = StationSummaryFile(
    filename="RE_2045_Scenario1_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="NT",
    sql_tablename="public.station_summary_2045s1_nt",
)
# ----------Scenario 2 ----------------------------------------------------------
s2_am = StationSummaryFile(
    filename="RE_2045_Scenario2_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="AM",
    sql_tablename="public.station_summary_2045s2_am",
)
s2_md = StationSummaryFile(
    filename="RE_2045_Scenario2_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="MD",
    sql_tablename="public.station_summary_2045s2_md",
)
s2_pm = StationSummaryFile(
    filename="RE_2045_Scenario2_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="PM",
    sql_tablename="public.station_summary_2045s2_pm",
)
s2_nt = StationSummaryFile(
    filename="RE_2045_Scenario2_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="NT",
    sql_tablename="public.station_summary_2045s2_nt",
)  # ----------Scenario 3 ----------------------------------------------------------
s3_am = StationSummaryFile(
    filename="RE_2045_Scenario3_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="AM",
    sql_tablename="public.station_summary_2045s3_am",
)
s3_md = StationSummaryFile(
    filename="RE_2045_Scenario3_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="MD",
    sql_tablename="public.station_summary_2045s3_md",
)
s3_pm = StationSummaryFile(
    filename="RE_2045_Scenario3_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="PM",
    sql_tablename="public.station_summary_2045s3_pm",
)
s3_nt = StationSummaryFile(
    filename="RE_2045_Scenario3_NewFare_RegRail_Trip_Stats.xlsx",
    skiprows=4,
    sheetname="NT",
    sql_tablename="public.station_summary_2045s3_nt",
)

station_summary_files = [
    nobuild_2045_am,
    s1_am,
    s1_md,
    s1_pm,
    s1_nt,
    s2_am,
    s2_md,
    s2_pm,
    s2_nt,
    s3_am,
    s3_md,
    s3_pm,
    s3_nt,
]
