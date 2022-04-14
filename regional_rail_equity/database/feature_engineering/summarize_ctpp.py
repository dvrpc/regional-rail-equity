from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_title


@print_title("GENERATING A SUMMARY OF THE CTPP EQUITY TABLES")
def summarize_ctpp_data(db: Database):
    """
    Execute a query that combines all of the raw CTPP
    tables into a single table with necessary values

    Summary includes:
        - percent of population that does not speak english at home

    To Do:
        - income
        - race
        - vehicles available
    """

    query_for_new_table = """
        with ctpp_taz_shapes as (
            select
                name,
                split_part(split_part(name, ',', 1), ' ', 2)::int as taz_id,
                geom
            from
                data.ctpp_poverty_by_household 
        ),
        pa_english as (
            select name,
                case when est_total_persons > 0 then
                    (1 - (est_english_speakers_five_over / est_total_persons)) * 100
                else null end as pct_non_english
            from data.pa_language_at_home 
        ),
        nj_english as (
            select name,
                case when est_total_persons > 0 then
                    (1 - (est_english_speakers_five_over / est_total_persons)) * 100
                else null end as pct_non_english
            from data.nj_language_at_home 
        ),
        english as (
            select * from pa_english
            union
            select * from nj_english
        ),
        poverty as (
            select name,
                case when est_below_100pct_poverty_status > 0 then 
                    est_below_100pct_poverty_status / est_total_poverty_status * 100
                else null end as below_100pct_poverty
            from data.ctpp_poverty_by_household
        ),
        pa_nonmotorized as (
            select name,
                case when est_total_vehicles_available  > 0 then 
                    (est_zero_vehicles_available / est_total_vehicles_available)  * 100
                else null end as nonmotorized
            from data.pa_vehicles_available
        ),
        nj_nonmotorized as (
            select name,
                case when est_total_vehicles_available  > 0 then 
                    (est_zero_vehicles_available / est_total_vehicles_available)  * 100
                else null end as nonmotorized
            from data.nj_vehicles_available 
        ),
        nonmotorized as (
            select * from pa_nonmotorized
            union
            select * from nj_nonmotorized
        ),
        nonwhite as (
            select name,
                case when est_white_alone_non_hispanic  > 0 then 
                    (1- (est_white_alone_non_hispanic  / est_total_persons))  * 100
                else null end as nonwhite
            from data.ctpp_minority_by_person
            )
        select
            s.name, s.taz_id, s.geom,
            e.pct_non_english,  
            width_bucket(e.pct_non_english, 0, 100, 10) as bucket_pct_non_english,
            p.below_100pct_poverty, 
            width_bucket(p.below_100pct_poverty, 0, 100, 10) as bucket_below_100pct_poverty,
            n.nonmotorized,
            width_bucket(n.nonmotorized, 0, 100, 10) as bucket_non_motorized,
            nw.nonwhite,
            width_bucket(nw.nonwhite, 0, 100, 10) as bucket_nonwhite
        from ctpp_taz_shapes s
        full outer join english e on s.name = e.name
        full outer join poverty p on s.name = p.name
        full outer join nonmotorized n on s.name = n.name
        full outer join nonwhite nw on s.name = nw.name;
    """

    db.gis_make_geotable_from_query(query_for_new_table, "ctpp.summary", "POLYGON", 26918)

    bucket_columns = [
        "bucket_nonwhite",
        "bucket_pct_non_english",
        "bucket_non_motorized",
        "bucket_below_100pct_poverty",
    ]

    for col in bucket_columns:

        query = f"""
            update ctpp.summary
            set {col} = 10
            where {col} > 10;
        """

        db.execute(query)


if __name__ == "__main__":
    summarize_ctpp_data(db)
