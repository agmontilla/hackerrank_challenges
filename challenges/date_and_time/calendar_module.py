""" Calendar module challenge. """
import calendar


def get_day_name(year: int, month: int, day: int) -> str:
    """Get day name."""
    day_names = calendar.weekheader(10).split()
    return day_names[calendar.weekday(year, month, day)].upper()


def main() -> None:
    """Main function."""
    month, day, year = list(map(int, input().split()))
    day_name = get_day_name(year, month, day)
    print(day_name)


if __name__ == "__main__":
    main()
