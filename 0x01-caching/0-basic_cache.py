#!/usr/bin/env python3
""" This module inherits from the basic cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from a parent class
    """

    def __init__(self) -> None:
        """ Constructor method
        """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to cache
        """
        if key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns a key to when called
        """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
