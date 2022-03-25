from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_title


# TODO: for the datasets that were downloaded separately for NJ and PA,
##      merge them together into a singular table that has both states combined


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
                data.ctpp_language_at_home 
        ),
        english as (
            select name,
                case when est_total > 0 then
                    (1 - (est_english / est_total)) * 100
                else null end as pct_non_english
            from data.ctpp_language_at_home 
        )
        select
            s.name, s.taz_id, s.geom,
            e.pct_non_english,
            width_bucket(e.pct_non_english, 0, 100, 5) as bucket_pct_non_english
        from ctpp_taz_shapes s
        full outer join english e on s.name = e.name
    """

    query = f"""
        update
            ctpp.summary
        set
            bucket_pct_non_english = 5
        where
            bucket_pct_non_english > 5;
    """

    db.gis_make_geotable_from_query(query_for_new_table, "ctpp.summary", "POLYGON", 26918)
    db.execute(query)


if __name__ == "__main__":
    summarize_ctpp_data(db)
