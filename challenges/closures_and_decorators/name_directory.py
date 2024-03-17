""" Name Directory """
from typing import Annotated, Callable, Generator

Person = Annotated[tuple[str, str, str, str], "Person tuple with name, last name, age and gender"]


def person_lister(f: Callable) -> Callable:
    """Person lister function"""

    def inner(people: list[Person]) -> Generator[str, None, None]:
        """Convert the people list into a string generator and sort it by age"""
        for person in sorted(people, key=lambda person: int(person[2])):
            yield f(person)

    return inner


def name_format(person: Person) -> str:
    """Format the name of the person"""
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


# I don't use the standard decorator syntax because I want to test the name_format function
# But there's no way to patch the decorator because both the decorator and the function are in the same module
# Here I found some helpful links to understand the way to patch a decorator but I didn't find a way to do it
# - https://dev.to/stack-labs/how-to-mock-a-decorator-in-python-55jc
# - https://stackoverflow.com/questions/7667567/can-i-patch-a-python-decorator-before-it-wraps-a-function/7667621#7667621
# - https://stackoverflow.com/questions/15698425/overriding-decorator-during-unit-test-in-python/15701244#15701244
# And here I found a helpful link to understand how the decorator works
# - https://gist.github.com/Zearin/2f40b7b9cfc51132851a
name_format_ = person_lister(name_format)


def main() -> None:
    """Main functions"""
    people = [input().split() for i in range(int(input()))]
    print(*name_format_(people), sep="\n")


if __name__ == "__main__":
    main()
