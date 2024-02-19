# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Power Mod Power """


class PowerModPower:
    """ Class to solve the problem """
    @staticmethod
    def get_power_modpower(a: int, b: int, c: int) -> None:
        """ Method to get the power and modpower """
        print(f'{pow(a, b)}\n{pow(a, b, c)}')


def main() -> None:
    """ Main function """
    a, b, c = int(input()), int(input()), int(input())
    PowerModPower.get_power_modpower(a, b, c)


if __name__ == "__main__":
    main()
