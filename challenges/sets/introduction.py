""" Introduction to Sets """


def average(array: list) -> float:
    """Returns the average of the unique elements in the array"""
    result: float = sum(set(array)) / len(set(array))
    return result


def main() -> None:
    """Main function"""
    _ = int(input())
    arr = list(map(int, input().split()))
    print(average(arr))


if __name__ == "__main__":
    main()
