""" Find Angle MBC """
import math


class AngleMBC:
    """Class to find the angle MBC"""

    def __init__(self, ab: int, bc: int) -> None:
        self.ab = ab
        self.bc = bc

    def __str__(self) -> str:
        """String representation"""
        angle_theta = round(math.degrees(math.atan(self.ab / self.bc)))
        return f"{angle_theta}°"


def main() -> None:
    """Main function"""
    ab, bc = int(input()), int(input())
    angle_mbc = AngleMBC(ab, bc)
    print(angle_mbc)


if __name__ == "__main__":
    main()
