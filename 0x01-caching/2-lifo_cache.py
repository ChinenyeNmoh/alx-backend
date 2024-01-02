#!/usr/bin/python3
"""
lifo caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching system class
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.popitem()
            discarded_key, _ = self.cache_data.popitem()
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
