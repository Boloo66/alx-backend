#!/usr/bin/env python3
""" This module inherits from the basic cache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from a parent class
    """

    def __init__(self):
        """ Constructor method
        """
        # super().__init__()
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Adds an item to cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
        pass

    def get(self, key):
        """ Returns a key to when called
        """
        if key in self.cache_data.keys() and key is not None:
            return self.cache_data.get(key)
        return None
