#!/usr/bin/env python3
"""
lifo_cache.py

Module: LIFOCache
-----------------
This module implements a caching system using a Last-In,
First-Out (LIFO) policy.
The `LIFOCache` class inherits from the base `BaseCaching`
class and enforces a maximum limit on the number of
items it can cache. When the cache reaches this limit,
the most recently added item is discarded to make space for
new entries.

Classes:
--------
LIFOCache(BaseCaching):
    Implements a LIFO-based caching system with a maximum item limit.
    The class stores items in the order they are
    added, discarding the most recent item when
    the cache reaches its maximum capacity.

Usage:
------
    To use this caching system, create an instance of `LIFOCache`,
    and use the `put` method to store items and
    the `get` method to retrieve items by key.
    If the cache exceeds its limit, the most recently added
    item is removed,
    and a message indicating the discarded key is printed.

Example:
--------
    cache = LIFOCache()
    cache.put("A", "Apple")
    cache.put("B", "Banana")
    cache.put("C", "Cherry")
    print(cache.get("B"))  # Output: "Banana"
    cache.put("D", "Date")  # If MAX_ITEMS is 3, this
    triggers removal of "C"
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that follows the Last-In,
    First-Out (LIFO) replacement policy,
    where the most recently added item is removed when
    the cache exceeds its item limit.

    Attributes:
    -----------
    cache_data : dict
        Inherited from BaseCaching, used to store cached
        items in a dictionary format.

    Methods:
    --------
    put(key, item):
        Stores the item in cache_data under the specified key.
        If the cache exceeds the maximum number of items (MAX_ITEMS),
        the most recently added item is removed (LIFO policy).
        If key or item is None, the method does nothing.
        Prints "DISCARD: {key}" when an item is discarded.

    get(key):
        Retrieves the item stored under
          the specified key in cache_data.
        Returns None if the key is None or does
          not exist in cache_data.
    """

    def __init__(self):
        """
        Initializes an instance of LIFOCache,
        setting up an empty cache.
        Inherits the initializer from the BaseCaching class.
        """
        super().__init__()
        self.modification_order = []

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

        # If key is already in cache, remove it from the modification order
        if key in self.cache_data:
            self.modification_order.remove(key)

        # Add or update the item in cache
        self.cache_data[key] = item
        # Track modification order
        self.modification_order.append(key)

        # Check if we need to discard the last modified item due to cache limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_modified_key = self.modification_order[-2]
            del self.cache_data[last_modified_key]
            self.modification_order.remove(last_modified_key)
            print(f"DISCARD: {last_modified_key}")

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
            return self.cache_data.get(key)
        return None
