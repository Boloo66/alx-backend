#!/usr/bin/env python3
""" This module inherits from the basic cache module
"""

# from base_caching import BaseCaching
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from a parent class
    """

    def __init__(self):
        """ Constructor method
        """
        super().__init__()
        # BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if item is None or key is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
