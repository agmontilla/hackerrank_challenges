""" Ordered Dict Challenge """

from collections import OrderedDict


def get_summary(transactions: int) -> dict:
    """Get the summary of the transactions"""
    bill: dict = OrderedDict()
    for _ in range(transactions):
        data = input().split()
        k, v = " ".join(data[:-1]), int(data[-1])
        bill[k] = bill.get(k, 0) + v

    return bill


def main() -> None:
    """Main function"""
    transactions = int(input())
    bill = get_summary(transactions)

    print(*(f"{k} {v}" for k, v in bill.items()), sep="\n")


if __name__ == "__main__":
    main()
