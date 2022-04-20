from dataclasses import dataclass


@dataclass
class StationSummaryFile:
    filename: str
    skiprows: int
    sql_tablename: str


nobuild_2045_am = StationSummaryFile(
    filename="2045_NoBld_AM_from_home_only_Trip_Stats_by_Station.xlsx",
    skiprows=4,
    sql_tablename="public.station_summary_2045nobuild_am",
)


station_summary_files = [
    nobuild_2045_am,
]
