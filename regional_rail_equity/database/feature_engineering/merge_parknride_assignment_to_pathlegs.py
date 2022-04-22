from regional_rail_equity import db

new_tablename = "computed.existing2019am_path_legs_with_assignment"
raw_pathlegs_table = "existing_2019am_home_to_dest_zone_fullpath"
assigned_parkandride_table = "computed.test_pnr_assignment"

if __name__ == "__main__":

    query = f"""
        drop table if exists {new_tablename};

        create table {new_tablename} as 

        with non_parkandride as (
            select
                origzoneno,
                destzoneno,
                odtrips,
                faretw,
                minutes,
                null as via_parknride
            from {raw_pathlegs_table}
            where origzoneno::int < 90000
        ),
        parkandride as (
            select
                true_origzoneno as origzoneno,
                destzoneno,
                sum(odtrips) as odtrips,
                faretw,
                minutes,
                origzoneno as via_parknride
            from {assigned_parkandride_table}
            group by
                true_origzoneno, destzoneno, faretw, minutes, origzoneno
        )
        select * from non_parkandride 
        union select * from parkandride
    """

    db.execute(query)
