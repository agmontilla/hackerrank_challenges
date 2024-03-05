""" Any or All Challenge

The idea of this challenge is to find a palindrome number in a list of numbers.
Also, they challenge you to solve it using 3 lines of code or less.

My simple solution was:
```python
if __name__ == "__main__":
    _, data = input(), list(map(int, input().split()))
    print(all(elem > 0 for elem in data) and any(filter(lambda x: True if str(x) == str(x)[::-1] else False, data)))
```

But I want to code it in a more readable way, so I did it:
"""


def is_palindrome(number: int) -> bool:
    """Check if a number is a palindrome"""
    return str(number) == str(number)[::-1]


def all_positive(data: list[int]) -> bool:
    """Check if all elements in the list are positive"""
    return all(elem > 0 for elem in data)


def main() -> None:
    """Main function"""
    _, data = input(), list(map(int, input().split()))
    print(all_positive(data) and any(is_palindrome(number) for number in data))


if __name__ == "__main__":
    main()
