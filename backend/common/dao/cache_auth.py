import redis


class Cache_Auth:
    def __init__(self):
        self.pool = redis.ConnectionPool(
            host="redis",
            port=6379,
            decode_responses=True,
        )
        self.r = redis.Redis(connection_pool=self.pool)
