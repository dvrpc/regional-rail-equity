from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_title

ALL_SCHEMAS = ["computed", "ctpp"]


@print_title("CREATING NEW SCHEMAS")
def create_schemas(db: Database) -> None:
    """
    Create schemas that will be needed later

    Arguments:
        db (Database): analysis database
    """

    for schema in ALL_SCHEMAS:
        db.schema_add(schema)


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
        ),
        poverty as (
            select name,
                case when est_below_100pct_poverty_status > 0 then 
                    est_below_100pct_poverty_status / est_total_poverty_status * 100
                else null end as below_100pct_poverty
            from data.ctpp_poverty_by_household
        ),
        nonmotorized as (
            select name,
                case when est_drove_alone > 0 then 
                    (1- (est_drove_alone  / est_total))  * 100
                else null end as nonmotorized
            from data.ctpp_travel_mode
        ),
        black_alone as (
            select name,
                case when est_black_alone  > 0 then 
                    est_black_alone  / est_all_races  * 100
                else null end as black_alone
            from data.ctpp_race_all_people 
        ),
        nonwhite as (
            select name,
                case when est_black_alone  > 0 then 
                    (1- (est_white_alone  / est_all_races))  * 100
                else null end as nonwhite
            from data.ctpp_race_all_people
        )
        select
            s.name, s.taz_id, s.geom,
            e.pct_non_english,  
            width_bucket(e.pct_non_english, 0, 100, 10) as bucket_pct_non_english,
            p.below_100pct_poverty,
            width_bucket(p.below_100pct_poverty, 0, 100, 10) as bucket_below_100pct_poverty,
            n.nonmotorized,
            width_bucket(n.nonmotorized, 0, 100, 10) as bucket_non_motorized,
            b.black_alone,
            width_bucket(b.black_alone, 0, 100, 10) as bucket_black_alone,
            nw.nonwhite,
            width_bucket(nw.nonwhite, 0, 100, 10) as bucket_nonwhite
        from ctpp_taz_shapes s
        full outer join english e on s.name = e.name
        full outer join poverty p on s.name = p.name
        full outer join nonmotorized n on s.name = n.name
        full outer join black_alone b on s.name = b.name
        full outer join nonwhite nw on s.name = nw.name;
    """

    query = f"""
        update
            ctpp.summary
        set
            bucket_pct_non_english = 5
        where
            bucket_pct_non_english > 5;
    """

    db.gis_make_geotable_from_query(
        query_for_new_table, "ctpp.summary", "POLYGON", 26918
    )
    db.execute(query)


@print_title("EXTRACTING DVRPC PA COUNTIES FROM MULTI-STATE COUNTY LAYER")
def clip_counties(db: Database):
    query = """
        select * from data.dvrpc_counties
        where
            state_name = 'Pennsylvania'
        and
            dvrpc_reg = 'Yes'
    """
    db.gis_make_geotable_from_query(query, "data.dvrpc_pa_counties", "POLYGON", 26918)


if __name__ == "__main__":
    create_schemas(db)
    summarize_ctpp_data(db)
    clip_counties(db)
