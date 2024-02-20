""" Loops """


def square(n: int) -> None:
    """ A function to print the square of numbers. """
    for number in range(n):
        print(f"{number ** 2}")


if __name__ == "__main__":
    square(int(input()))
