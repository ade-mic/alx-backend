#!/usr/bin/env python3
"""
basic_cache.py

Module: BasicCache
------------------
This module implements a simple caching system, `BasicCache`,
 which inherits from a base class, `BaseCaching`.
The `BasicCache` class does not impose a limit on the number
 of items it can hold in the cache.

Classes:
--------
BasicCache(BaseCaching):
    Implements a basic, unlimited caching system using a dictionary
      to store key-value pairs.
    The class provides methods to put items into the cache and
      retrieve them by key.

Usage:
------
    To use this caching system, create an instance of `BasicCache`
      and use `put` to store items and
    `get` to retrieve items.

Example:
--------
    cache = BasicCache()
    cache.put("A", "Apple")
    print(cache.get("A"))  # Output: "Apple"
"""
from typing import Any, Optional
BaseCaching = __import__('base_cashing').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple caching system that inherits from
      BaseCaching.

    This caching system stores key-value pairs in an unrestricted
    dictionary, meaning there is no limit on the number of items
      it can cache.

    Attributes:
    -----------
    cache_data : dict
        Inherited from BaseCaching, used to store cache items in
          a dictionary format.

    Methods:
    --------
    put(key, item):
        Stores the item in cache_data under the specified key.
        If either key or item is None, the method does nothing.

    get(key):
        Retrieves the item stored under the specified key in
          cache_data.
        Returns None if the key is None or does not exist in
          cache_data.
    """

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
            Does not return any value. If key or item is None,
              performs no action.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key: Optional[str]) -> Optional[Any]:
        """
        Retrieves the item stored under the specified key in
          cache_data.

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
