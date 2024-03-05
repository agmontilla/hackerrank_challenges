""" Athlete Sort Challenge """


def order_by_athlete(sheet: list, attribute: int) -> list[tuple[int]]:
    """Order by athlete"""
    return sorted(sheet, key=lambda athlete: athlete[attribute])


def main() -> None:
    """Main function"""
    rows, attributes = tuple(map(int, input().split()))
    sheet = []
    for _ in range(rows):
        sheet.append(tuple(map(int, input().split()[:attributes])))

    sort_option = int(input())

    print("\n".join([" ".join(map(str, athlete)) for athlete in order_by_athlete(sheet, sort_option)]))


if __name__ == "__main__":
    main()
