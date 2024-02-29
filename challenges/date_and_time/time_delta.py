""" Time delta challenge """

from datetime import datetime as dt

FORMAT = "%a %d %b %Y %H:%M:%S %z"


def time_delta(t1: str, t2: str) -> str:
    """Returns the absolute difference in seconds between two timestamps"""
    d1, d2 = dt.strptime(t1, FORMAT), dt.strptime(t2, FORMAT)
    return str(int(abs(d1 - d2).total_seconds()))


def main() -> None:
    """Main function"""
    t = int(input())
    timestamp_pairs = [(input(), input()) for _ in range(t)]

    results = [time_delta(t1, t2) for t1, t2 in timestamp_pairs]

    print(*results, sep="\n")


if __name__ == "__main__":
    main()
