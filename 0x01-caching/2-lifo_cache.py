#!/usr/bin/python3
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key = self.stack.pop()
            del self.cache_data[most_recent_key]
            print("DISCARD: {}\n".format(most_recent_key))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
