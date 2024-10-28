#!/usr/bin/env python3
"""
module for pagination
"""
import csv
import math
from typing import List, Tuple


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
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            if start_index >= len(dataset):
                return []
            # remove the header row bt adding 1
            return dataset[start_index + 1:end_index + 1]
