#!/usr/bin/env python3
"""
fifo_cache.py

Module: FIFOCache
-----------------
This module implements a caching system using a First-In,
First-Out (FIFO) policy.
The `FIFOCache` class inherits from the base `BaseCaching` class and
imposes a limit on the number of items it can cache.
When the cache reaches its maximum limit (defined in `BaseCaching.
MAX_ITEMS`), the oldest item added to the cache
is discarded to make room for new entries.

Classes:
--------
FIFOCache(BaseCaching):
    Implements a FIFO-based caching system with a maximum item limit.
    It retains items in the order they are added,
    discarding the oldest item when the cache limit is reached.

Usage:
------
    To use this caching system, create an instance of `FIFOCache`,
    and use the `put` method to store items and the
    `get` method to retrieve items by key. If the cache exceeds its
    limit, the oldest item is removed, and a message
    indicating the discarded key is printed.

Example:
--------
    cache = FIFOCache()
    cache.put("A", "Apple")
    cache.put("B", "Banana")
    cache.put("C", "Cherry")
    print(cache.get("A"))  # Output: "Apple"
    cache.put("D", "Date")  # If MAX_ITEMS is 3, this triggers
    removal of "A"
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that follows the First-In,
    First-Out (FIFO) replacement policy,
    where the oldest item is removed when the cache exceeds
    its item limit.

    Attributes:
    -----------
    cache_data : dict
        Inherited from BaseCaching, used to store cached items
        in a dictionary format.

    Methods:
    --------
    put(key, item):
        Stores the item in cache_data under the specified key.
        If the cache exceeds the maximum number of items (MAX_ITEMS),
        the oldest item is removed (FIFO policy).
        If key or item is None, the method does nothing.
        Prints "DISCARD: {key}" when an item is discarded.

    get(key):
        Retrieves the item stored under the specified key in cache_data.
        Returns None if the key is None or does not exist in cache_data.
    """

    def __init__(self):
        """
        Initializes an instance of FIFOCache, setting up an empty cache.
        Inherits the initializer from the BaseCaching class
        """
        super().__init__()

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
            If the cache exceeds MAX_ITEMS, the oldest entry is
            discarded (FIFO).
            If key or item is None, does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")

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
