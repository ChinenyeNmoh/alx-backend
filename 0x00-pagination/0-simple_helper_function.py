#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page: int, page_size: int):
    """
    0. Simple helper function
    """
    return (page-1)*page_size, page*page_size
