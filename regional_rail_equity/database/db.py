from pg_data_etl import Database

from .env_vars import DATABASE_URL

db = Database.from_uri(DATABASE_URL)
