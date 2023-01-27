#!/usr/bin/env python3
""" This module inherits from the basic cache module
"""

# from base_caching import BaseCaching
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines LIFO caching system
    """

    def __init__(self):
        """ Initialzer for the parent class
        """
        super().__init__()
        self.out = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.out[-1]))
                del self.cache_data[self.out[-1]]
                del self.out[-1]
            self.out.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the item of a cache"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
