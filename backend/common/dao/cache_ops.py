from common.dao.cache_auth import Cache_Auth
import json


class Cache_Ops:
    def __init__(self):
        self.cache_auth = Cache_Auth()

    def exists(self, key):
        return self.cache_auth.r.exists(key)

    def set(self, key, deserialized_val_list):
        # NOTE: value is passed in deserialized form and is serialzed before being set
        # this helps to deal with complex or nested data structures
        serialized_val_list = json.dumps(deserialized_val_list)
        self.cache_auth.r.set(key, serialized_val_list)
        self.cache_auth.r.expire(key, 5)

    def get(self, key):
        # if value doesn't exist in cache
        if not self.exists(key):
            return None
        serialized_val_list = self.cache_auth.r.get(key)
        
        # if value is null despite key being present
        if serialized_val_list is None:
            return None

        # NOTE: value is serialized when retrieved from cache but is deserialized during returning
        deserialized_val_list = json.loads(serialized_val_list)
        return deserialized_val_list
