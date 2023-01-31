import psycopg
import yaml
from yaml.loader import SafeLoader


class DB_Auth:
    def __init__(self):
        # Open the file and load the file
        config_file = "./.config/db/config.yaml"
        with open(config_file) as cf:
            conn_dict = yaml.load(cf, Loader=SafeLoader)

        self.conn = psycopg.connect(
            "host={} dbname={} user={} password={} port={}".format(
                conn_dict["host"],
                conn_dict["dbname"],
                conn_dict["user"],
                conn_dict["password"],
                conn_dict["port"],
            )
        )
        print("conn created")

    def __del__(self):
        self.conn.close()
