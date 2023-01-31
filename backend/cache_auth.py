import redis
import yaml
from yaml.loader import SafeLoader


class Cache_Auth:
    def __init__(self):
        config_file = "./.config/cache/config.yaml"
        with open(config_file) as cf:
            conn_dict = yaml.load(cf, Loader=SafeLoader)
        self.pool = redis.ConnectionPool(
            host=conn_dict["host"],
            port=conn_dict["port"],
            decode_responses=conn_dict["decode_responses"],
        )
        self.r=redis.Redis(connection_pool=self.pool)
