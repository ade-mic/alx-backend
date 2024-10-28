#!/usr/bin/env python3
"""
module for pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end indexes for pagination..
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from a CSV file.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List[str]]: A list of rows corresponding
            to the requested page.
        """

        assert isinstance(page, int) and page > 0,\
            "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing pagination metadata
        and data for the specified page.

        Parameters:
            page (int): The current page number (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary with the following key-value pairs:
                - page_size (int): The length of the returned dataset page.
                - page (int): The current page number.
                - data (List[Any]): The dataset page for the
                    specified page and page_size.
                - next_page (Optional[int]): The number of the
                     next page if it exists; None otherwise.
                - prev_page (Optional[int]): The number of the
                    previous page if it exists; None otherwise.
                - total_pages (int): The total number of pages in
                     the dataset.
        """
        total_items = len(self.dataset())
        total_pages = (total_items + page_size - 1) // page_size
        data = self.get_page(page, page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
