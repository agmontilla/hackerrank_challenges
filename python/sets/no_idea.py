# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Happiness """


def calculate_happines(array: list, set_a: set, set_b: set) -> int:
    """Calculate the happiness"""
    happines = 0
    for elem in array:
        if elem in set_a:
            happines += 1
        elif elem in set_b:
            happines -= 1
    return happines


def main() -> None:
    """Main function"""
    arr_dim, set_dim = map(int, input().split())
    arr = list(map(int, input().split()))[:arr_dim]
    set_a, set_b = [set(map(int, input().split()[:set_dim])) for _ in range(2)]

    print(calculate_happines(arr, set_a, set_b))


if __name__ == "__main__":
    main()
