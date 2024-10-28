#!/usr/bin/env python3
"""
The module contain function index_range  two integer arguments
page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Indexed a list for pagination.
    Args:
        page(int): the page to be displayed
        page_size(int): the number of item in the page
    Returns:
        (start_index, end_index): a tuple containing the start index
        and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
