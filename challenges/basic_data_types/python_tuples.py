""" Python Tuples """


def get_hash(integer_list: tuple[int, ...]) -> int:
    """Return the hash of the integer_list."""
    return hash(integer_list)


def main() -> None:
    """Main function"""
    _ = int(input())
    integer_list = tuple(map(int, input().split()))
    print(get_hash(integer_list))


if __name__ == "__main__":
    main()
