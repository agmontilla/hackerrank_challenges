from typing import List

COORDINATES = List[List[int]]


def get_all_possible_cuboid_dim(
    x_coord: int, y_coord: int, z_coord: int, N: int
) -> COORDINATES:

    coordinates = [
        [i, j, k]
        for i in range(x_coord + 1)
        for j in range(y_coord + 1)
        for k in range(z_coord + 1)
        if i + j + k != N
    ]

    return coordinates


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print("{}".format(get_all_possible_cuboid_dim(x, y, z, n)))
