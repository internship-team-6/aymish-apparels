import redis


class Cache_Auth:
    def __init__(self):
        # connect to cache with below connection details
        # use connection pool in order to reuse connections
        self.pool = redis.ConnectionPool(
            host="redis",
            port=6379,
            decode_responses=True,
        )

        self.r = redis.Redis(connection_pool=self.pool)
