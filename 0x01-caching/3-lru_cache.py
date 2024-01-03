#!/usr/bin/python3
"""
lru caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system class
    """

    def __init__(self):
        """ Initialize a new FIFOCache. """
        super().__init__()
        self.list_keys = []

    def put(self, key, item):
        """ Function to assing to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.list_keys:
                self.list_keys.append(key)
            else:
                self.list_keys.append(self.list_keys.pop(
                    self.list_keys.index(key)))
            if len(self.list_keys) > BaseCaching.MAX_ITEMS:
                # LRU algorithm
                lru_discard = self.list_keys.pop(0)
                del self.cache_data[lru_discard]
                print("DISCARD: {}".format(lru_discard))

    def get(self, key):
        """ Function to return the value: item by key """
        if key is not None and key in self.cache_data:
            self.list_keys.append(self.list_keys.pop(
                self.list_keys.index(key)))
            return self.cache_data[key]
        return None
