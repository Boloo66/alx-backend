#!/usr/bin/env python3
""" This module inherits from the basic cache module
"""

# from base_caching import BaseCaching
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                discarded_ele = self.keys_list[0]
                self.cache_data.pop(discarded_ele, None)
                del self.keys_list[0]

                print("DISCARD: {}".format(discarded_ele))
            self.cache_data[key] = item
            self.keys_list.append(key)

    def get(self, key):
        """
        Returns the item of a Cached key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
