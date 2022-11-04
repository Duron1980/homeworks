def create_square(number_characters) -> print:
    for character in range(number_characters):
        if character == 0 or character == number_characters-1:
            [print('# ', end='') for character in range(number_characters)]
        else:
            [print('# ',end='') if character == 0 or character == number_characters-1 else print('  ',end='') for character in range(number_characters)]
        print('')

def main(number_characters: int):
    create_square(number_characters)


if __name__ == '__main__':
    while True:
        try:
            number_characters = int(input((' How many characters # must be in side square  - ')))
            break
        except ValueError:
            print(' You entere wrang value ')
            continue
    main(number_characters)
