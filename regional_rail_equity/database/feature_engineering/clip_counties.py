from pg_data_etl import Database

from regional_rail_equity import db
from regional_rail_equity.helpers import print_title


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
    clip_counties(db)
