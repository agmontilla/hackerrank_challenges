"""Mod Divmod"""


class ModDivmod:
    """ Class to solve the problem """
    @staticmethod
    def get_mod_divmod(a: int, b: int) -> None:
        """ Method to get the mod and divmod """
        print(f'{a//b}\n{a%b}\n{(a//b, a%b)}')


def main() -> None:
    """ Main function """
    a, b = int(input()), int(input())
    ModDivmod.get_mod_divmod(a, b)


if __name__ == "__main__":
    main()
