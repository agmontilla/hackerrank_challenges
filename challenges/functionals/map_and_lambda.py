"""" Map and Lambda Function Challenge

The idea of this challenge is to use the map function to generate a list of fibonacci numbers
and then use the lambda function to map the cube function to the list of fibonacci numbers.
But lambda assignment is not necessary and it is better to use the function directly (pylint and flake8 will complain about it).
For that reason, I disabled the unnecessary-lambda-assignment and E731 (do not assign a lambda expression, use a def).
"""

cube = lambda x: x**3  # pylint: disable=unnecessary-lambda-assignment # noqa: E731


def fibonacci(n: int) -> list[int]:
    """Return a list of fibonacci numbers"""
    a, b = 1, 0
    fibo_numbers = [0]
    for _ in range(n - 1):
        fibo_numbers.append(a)
        a, b = a + b, a

    return [] if n == 0 else fibo_numbers


def main() -> None:
    """Main function"""
    n = int(input())
    print(list(map(cube, fibonacci(n))))


if __name__ == "__main__":
    main()
