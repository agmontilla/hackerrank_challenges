""" Write a function to check if a year is a leap year or not. """


def is_leap(year: int) -> bool:
    """ A function to check if a year is a leap year or not. """
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        if year % 100 != 0 and year % 400 != 0:
            leap = True
    return leap


if __name__ == "__main__":
    print(is_leap(int(input())))
