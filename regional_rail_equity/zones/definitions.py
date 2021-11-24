from dataclasses import dataclass
from pg_data_etl import Database

from regional_rail_equity import db


@dataclass
class ZoneDefinition:
    """
    Class that defines a set of TAZs which constitute a larger named zone

    Usage:
        myzone = ZoneDefinition('The Name', db, (1, 2, 3, 4))
        myzone.save_to_db()
    """

    name: str
    db: Database
    ids: tuple[int]
    tablename: str = "public.zones"

    def confirm_db_table_exists(self):
        create_table_query = f"""
            CREATE TABLE {self.tablename} (
                zone_name       text,
                tazt            varchar(40)
            );
            CREATE INDEX ON {self.tablename}(zone_name);
        """
        if self.tablename not in self.db.tables():
            self.db.execute(create_table_query)

    def save_to_db(self):
        self.confirm_db_table_exists()

        # If this zone has already been defined, remove the old values before adding new ones
        if self.name in db.query(f"SELECT DISTINCT zone_name FROM {self.tablename}"):
            delete_query = f"""
                DELETE FROM {self.tablename}
                WHERE zone_name = '{self.name}';
            """
            self.db.execute(delete_query)

        # Insert the new zone IDs into the table
        insert_statement = f"INSERT INTO {self.tablename} VALUES "

        query_values = ", ".join([f"('{self.name}', {zone_id})" for zone_id in self.ids])

        insert_query = insert_statement + query_values + ";"

        self.db.execute(insert_query)


# fmt: off
center_city_full = ZoneDefinition("Center City - Girard to Washington", db, (2, 14, 20, 21, 26, 31, 66, 70, 72, 84, 86, 88, 90, 95, 108, 112, 132, 141, 405, 406, 842, 4, 5, 24, 32, 46, 53, 68, 81, 85, 94, 96, 102, 117, 119, 133, 137, 143, 3, 7, 18, 27, 36, 49, 58, 64, 89, 97, 104, 105, 109, 115, 124, 142, 402, 403, 37, 38, 48, 55, 61, 63, 69, 74, 75, 110, 125, 135, 33, 40, 41, 45, 50, 52, 56, 71, 80, 93, 99, 101, 107, 114, 130, 131, 136, 140, 846, 9, 10, 12, 15, 16, 19, 39, 60, 62, 65, 67, 73, 79, 82, 92, 98, 103, 106, 111, 118, 122, 126, 127, 139, 6, 11, 13, 28, 29, 44, 47, 59, 76, 77, 113, 116, 120, 121, 128, 134, 404, 1, 22, 25, 30, 34, 42, 43, 51, 54, 57, 78, 83, 87, 91, 100, 123, 129, 138, 8, 17, 23, 35))
center_city_small = ZoneDefinition("Center City - Vine to South", db, (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122))

ALL_ZONES = [center_city_full, center_city_small]


if __name__ == "__main__":
    for zone in ALL_ZONES:
        zone.save_to_db()
