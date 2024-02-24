""" List Comprehensions """
from typing import List

COORDINATES = List[List[int]]


def get_all_possible_cuboid_dim(x_coord: int, y_coord: int, z_coord: int, big_n: int) -> COORDINATES:
    """Get all possible coordinates of a cuboid"""
    coordinates = [[i, j, k] for i in range(x_coord + 1) for j in range(y_coord + 1) for k in range(z_coord + 1) if i + j + k != big_n]

    return coordinates


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(f"{get_all_possible_cuboid_dim(x, y, z, n)}")
