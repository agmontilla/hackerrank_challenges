from collections import Counter

if __name__ == "__main__":

    n = int(input())
    room_numbers = sorted(list(map(int, input().split())))
    uniques = set(room_numbers)

    captain_number = Counter(room_numbers).most_common()[-1][0]

    print(f'{captain_number}')
