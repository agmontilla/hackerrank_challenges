def main(n: int) -> None:
    # n is odd
    if n % 2 != 0:
        print("Weird")
    # n is even
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    pass


if __name__ == "__main__":

    n = int(input())
    main(n)
