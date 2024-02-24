""" Python Print """


def print_str(n: int) -> None:
    """A function to print the numbers from 1 to n."""
    for elem in range(n):
        print(elem + 1, end="")


if __name__ == "__main__":
    print_str(int(input()))
