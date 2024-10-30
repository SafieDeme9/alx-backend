#!/usr/bin/python3
"""Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """assign to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
