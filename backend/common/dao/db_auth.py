import psycopg
from psycopg.rows import dict_row


class DB_Auth:
    def __init__(self):
        # connect to database with below connection details
        # specify row_factory as dict_row in order for values to be returned in the dictionary format
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
        # specified closing of connection in destructor so that connection gets closed automatically at the time the object is destroyed
        self.conn.close()
