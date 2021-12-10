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
