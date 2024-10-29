#!/usr/bin/env python3
"""
    LFUCache is a caching system that follows the Least
    Frequently Used (LFU) caching algorithm.
    If the cache exceeds its capacity, it removes the
      least frequently used item.
    In case of a frequency tie, it uses the
      Least Recently Used (LRU) rule to determine which item to discard.
"""
from base_caching import BaseCaching
from typing import Any, Optional


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that follows
      the Least Frequently Used (LFU) caching algorithm.
    If the cache exceeds its capacity, it removes
      the least frequently used item.
    In case of a frequency tie, it uses the
      Least Recently Used (LRU) rule to determine which item to discard.
    """

    def __init__(self) -> None:
        """Initialize the LFUCache and call the parent
          class initializer."""
        super().__init__()
        # Dictionary to store the access frequency of each key
        self.frequency = {}
        # List to keep track of the access order of keys
        self.usage_order = []

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Store an item in the cache under the specified key.

        Parameters:
            key (Optional[str]): The key for the item to store.
            item (Optional[Any]): The value to store in the cache.

        If key or item is None, this method does nothing.
          If the number of items in
        cache_data exceeds BaseCaching.MAX_ITEMS,
          the least frequently used item
        is discarded, with ties broken by
          the Least Recently Used (LRU) rule.
        """
        if key is None or item is None:
            return

        # Update the cache and frequency if the key is already present
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If new entry and cache limit is exceeded,
            # evict least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used keys
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, freq in self.frequency.items()
                            if freq == min_freq]

                # Discard the LRU among the least frequently used keys
                lfu_key = next(k for k in self.usage_order if k in lfu_keys)
                self.usage_order.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add new item and set frequency to 1
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key: Optional[str]) -> Optional[Any]:
        """
        Retrieve the value associated with the specified
          key in the cache.

        Parameters:
            key (Optional[str]): The key of the item to retrieve.

        Returns:
            Optional[Any]: The value linked to the
              key if it exists, or None if the key is None
            or does not exist in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and usage order for the accessed key
        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
