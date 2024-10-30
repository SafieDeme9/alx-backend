#!/usr/bin/python3
"""FIFO cache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if BaseCaching.MAX_ITEMS < len(self.cache_data):
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
