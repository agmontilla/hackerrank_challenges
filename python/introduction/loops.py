def square(n: int) -> None:
    for number in range(n):
        print("{}".format(number ** 2))


if __name__ == "__main__":
    n = int(input())
    square(n)
