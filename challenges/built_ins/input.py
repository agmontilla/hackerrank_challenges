""" Built-in input() Challenge

I was not able to solve this challenge using literal_eval (it is supposed to be a safer version of eval).
So, I used eval instead.

Better explanation can be found [here](https://stackoverflow.com/questions/12080197/why-does-this-string-not-work-with-ast-literal-eval)
"""


def is_divisible_by(k: int, x: int, polinomial: str) -> bool:  # pylint: disable=unused-argument
    """Check if x is divisible by k"""
    return k == int(eval(polinomial))  # pylint: disable=eval-used


def main() -> None:
    """Main function"""
    x, k = tuple(map(int, input().split()))
    polinomial = input()

    print(is_divisible_by(k, x, polinomial))


if __name__ == "__main__":
    main()
