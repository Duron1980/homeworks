"""check string for polyndromism"""
def function_1(word: str)-> str:
    check_string = ''.join(letter for letter in word if letter.isalnum())
    return check_string


def function_2(word: str):
    if word[:] == word[::-1]:
        return print(f'Word {word} is polyndrom ')
    return print(f'Word {word} is not polyndrom ')


def function_3(word: str):
    """main controller"""
    check_str = check_input_string(word)
    chek_word_polyndromism(check_str)


if __name__ == '__main__':
    input_string = (input(' Enter word for chek polyndromism: ')).lower()
    main(input_string)
