""" This module contains utility functions for numpy challenges """


def get_entries() -> list[list[int]]:
    """Get entries from user input"""
    n, m = map(int, input().split())
    data = [list(map(int, input().split()))[:m] for _ in range(n)]
    return data
