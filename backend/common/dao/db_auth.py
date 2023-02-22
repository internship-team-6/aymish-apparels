import psycopg
from psycopg.rows import dict_row


class DB_Auth:
    def __init__(self):
        self.conn = psycopg.connect(
            "host={} dbname={} user={} password={} port={}".format(
                "postgres",
                "postgres",
                "manish",
                "manish",
                5432,
            ),
            row_factory=dict_row,
        )

    def __del__(self):
        self.conn.close()
