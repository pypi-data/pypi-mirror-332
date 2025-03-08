import time

class ResponseCache:
    def __init__(self, expiration=30):
        self.cache = {}
        self.expiration = expiration

    def get(self, key):
        """Retrieve from cache if not expired"""
        if key in self.cache:
            data, timestamp = self.cache[key]
            if time.time() - timestamp < self.expiration:
                return data
            del self.cache[key]
        return None

    def set(self, key, data):
        """Store data in cache"""
        self.cache[key] = (data, time.time())



