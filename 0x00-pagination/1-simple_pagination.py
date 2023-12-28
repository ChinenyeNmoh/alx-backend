#!/usr/bin/env python3
"""1. Simple pagination
"""
import csv
from typing import List


def index_range(page: int, page_size: int):
    """
    0. Simple helper function
    """
    return (page-1)*page_size, page*page_size


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
        """1. Simple pagination
        """
        if (
            not isinstance(page, int) or
            not isinstance(page_size, int) or
            page <= 0 or page_size <= 0
        ):
            raise AssertionError
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
