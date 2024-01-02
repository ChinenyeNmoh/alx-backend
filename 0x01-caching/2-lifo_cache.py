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
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()