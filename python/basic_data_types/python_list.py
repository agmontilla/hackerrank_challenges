from typing import Any, List


def run_option(option: str, collection: List, args: Any) -> None:

    # TODO: better implemention of this could be using hassatr/getattr functions

    if option == "insert":
        collection.insert(*args)
    elif option == "print":
        print(collection)
    elif option == "remove":
        collection.remove(*args)
    elif option == "append":
        collection.append(*args)
    elif option == "sort":
        collection.sort()
    elif option == "pop":
        collection.pop()
    elif option == "reverse":
        collection.reverse()
    else:
        raise ValueError("This option is not valid")


if __name__ == "__main__":
    N = int(input())
    data: List = []
    for _ in range(N):
        option, *line = input().split()
        args = list(map(int, line))
        run_option(option, data, args)
