from cache_auth import Cache_Auth
from pprint import pprint
import json


class Cache_Ops:
    def __init__(self):
        self.cache_auth = Cache_Auth()

    def exists(self, key):
        return self.cache_auth.r.exists(key)

    def set(self, key, deserialized_val_list):
        serialized_val_list = json.dumps(deserialized_val_list)
        self.cache_auth.r.set(key, serialized_val_list)

    def get(self, key):
        if not self.exists(key):
            return None
        serialized_val_list = self.cache_auth.r.get(key)
        if serialized_val_list is None:
            return None
        deserialized_val_list = json.loads(serialized_val_list)
        return deserialized_val_list
