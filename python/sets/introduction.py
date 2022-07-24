def average(array: list) -> float:
    return(sum(set(array))/len(set(array)))


def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    print(average(arr))


if __name__ == "__main__":
    main()
