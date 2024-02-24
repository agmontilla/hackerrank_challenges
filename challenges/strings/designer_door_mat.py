# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Designer Door Mat """

PART = ".|."
MINUS = "-"


def is_odd(n: int) -> bool:
    """Check if a number is odd"""
    if n % 2 == 0:
        raise ValueError(f"{n} is not a odd number")

    return True


def check_columns(rows: int, cols: int) -> bool:
    """Check if the columns are 3 times greater than rows"""
    if cols != 3 * rows:
        raise ValueError(f"We can not print because cols ({cols}) is not 3 times greater than rows ({rows})")

    return True


def print_dot(rows: int, cols: int) -> None:
    """Print the door mat"""
    if is_odd(rows) and check_columns(rows, cols):
        odd_numbers = [n for n in range(rows) if n % 2.0 != 0 and n < rows]

        for value in odd_numbers:
            print((value * PART).center(cols, MINUS))

        print("WELCOME".center(cols, MINUS))

        for value in reversed(odd_numbers):
            print((value * PART).center(cols, MINUS))


if __name__ == "__main__":
    N, M = input().split()
    print_dot(int(N), int(M))
