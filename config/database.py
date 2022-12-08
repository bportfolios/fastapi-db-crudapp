from psycopg2 import connect

DATABASE_URL = "postgresql://username:password@host:port/dbname"

connection = connect(DATABASE_URL)