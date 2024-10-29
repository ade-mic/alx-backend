#!/usr/bin/env python3
"""

This module defines the LRUCache class, which implements a caching system
based on the Least Recently Used (LRU) replacement policy.

The LRUCache class inherits from BaseCaching and uses a dictionary to manage
cached items, automatically discarding the least recently used item when
the cache exceeds its capacity.

Usage:
    To use this caching system, create an instance of LRUCache, and utilize
    the put and get methods to store and retrieve items from the cache.

"""

BaseCaching = __import__('base_cashing').BaseCaching


class LRUCache(BaseCaching):
    """
  LRUCache is a caching system that implements the Least Recently
    Used (LRU) replacement policy.

    This class inherits from BaseCaching and utilizes a dictionary
      to manage cached items.
    It automatically discards the least recently used item when the
      cache exceeds its capacity.

    Attributes:
        cache_data (dict): A dictionary to store cached items,
          inherited from BaseCaching.

    Methods:
        __init__(): Initializes the LRUCache and calls the parent
          class initializer to set up the cache.

        put(key, item):
            Stores an item in the cache under the specified key.

            Parameters:
                key (str): The key for the item to store.
                item (any): The value to store in the cache.

            If key or item is None, this method does not perform
              any action.
            If the number of items in cache_data exceeds BaseCaching
            .MAX_ITEMS,
            the least recently used item is discarded, and a message
              is printed indicating
            the discarded key.

        get(key):
            Retrieves the value associated with the specified
              key in the cache.

            Parameters:
                key (str): The key of the item to retrieve.

            Returns:
                any: The value linked to the key if it exists,
                  or None if the key is None
                or does not exist in cache_data.
    """

    def __init__(self):
        """
        Initializes an instance of LRUCache,
        setting up an empty cache.
        Inherits the initializer from the BaseCaching class.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Stores the item in cache_data under the specified key.

        Parameters:
        -----------
        key : str
            The key under which the item will be stored.
        item : any
            The value to be stored in cache_data.

        Returns:
        --------
        None
            If the cache exceeds MAX_ITEMS, the most recent
            entry is discarded (LIFO).
            If key or item is None, does nothing.
        """
        if key is None or item is None:
            return
        # Track most recently used order
        if key in self.cache_data:
            self.lru_order.remove(key)
        # Add or update the item in cache
        self.cache_data[key] = item
        self.lru_order.append(key)

        # Check if we need to discard the last recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recent_used_key = self.lru_order.pop(0)
            del self.cache_data[least_recent_used_key]
            print(f"DISCARD: {least_recent_used_key}")

    def get(self, key):
        """
        Retrieves the item stored under the specified key in cache_data.

        Parameters:
        -----------
        key : str
            The key of the item to retrieve.

        Returns:
        --------
        any or None
            Returns the value associated with the key in cache_data.
            Returns None if key is None or the key does not exist
            in cache_data.
        """
        if key:
            # Track most recently used order
            if key in self.cache_data:
                self.lru_order.remove(key)
                self.lru_order.append(key)

            return self.cache_data.get(key)
        return None
