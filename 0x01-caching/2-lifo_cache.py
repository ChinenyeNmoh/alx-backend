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
            if self.cache_data:
                discard = list(self.cache_data)[-1]
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(discard)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
