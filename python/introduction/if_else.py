""" A program to check if a number is weird or not. """


def main(n: int) -> None:
    """A function to check if a number is weird or not."""
    # n is odd
    if n % 2 != 0:
        print("Weird")
    # n is even
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == "__main__":
    main(int(input()))
