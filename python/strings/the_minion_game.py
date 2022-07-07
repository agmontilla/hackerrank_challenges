VOWELS = ['a', 'e', 'i', 'o', 'u']


def minion_game(string: str) -> None:

    length = len(string)
    vowel_score, consonant_score = 0, 0

    for idx, ch in enumerate(string):
        if ch.lower() in VOWELS:
            vowel_score += length - idx
        else:
            consonant_score += length - idx

    if vowel_score > consonant_score:
        print(f'Kevin {vowel_score}')
    elif vowel_score < consonant_score:
        print(f'Stuart {consonant_score}')
    else:
        print('Draw')


def main() -> None:
    s = input()
    minion_game(s)


if __name__ == '__main__':
    main()
