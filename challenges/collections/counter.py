""" Collections.Counter() challenge """

from collections import Counter


def get_profits(shoes: list, asks: list) -> int:
    """Get the total profit of the shop"""
    all_shoes = Counter(shoes)
    total = []

    for size_ask, price in asks:
        if all_shoes[size_ask]:
            all_shoes = all_shoes - (Counter([size_ask]))
            total.append(price)

    return sum(total)


def main() -> None:
    """Main function"""
    _, shoes = input(), list(map(int, input().split()))
    asks = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(get_profits(shoes, asks))


if __name__ == "__main__":
    main()
    # _, all_shoes = input(), Counter(list(map(int, input().split())))
    # total = []

    # for _ in range(int(input())):
    #     size_ask, price = tuple(map(int, input().split()))
    #     if all_shoes[size_ask]:
    #         all_shoes = all_shoes - (Counter([size_ask]))
    #         total.append(price)

    # print(f"{sum(total)}")
