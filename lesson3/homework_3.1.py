def creating_strings() -> list:
    strings = []
    while True:
        try:
            number_strings = int(input((' How many strings do you want enter - ')))
            break
        except ValueError:
            print(' You entere wrang value ')
            continue
    for i in range(number_strings):
        string = input(f' Enter {i + 1} string -  ')
        strings.append(string)
    return strings


def refactoring_string(STRINGS: list) -> print:
    result = [*(string[(len(string) // 2) - 1:(len(string) // 2) + 1] if len(string) % 2 == 0 else string[
        (len(string) // 2)] if len(string) % 2 != 0 else string for string in STRINGS)]
    print(*(f'Middle of {result.index(string) + 1} string is  - {string}' + '\n' for string in result))


def main():
    strings = creating_strings()
    refactoring_string(strings)


if __name__ == '__main__':
    main()
