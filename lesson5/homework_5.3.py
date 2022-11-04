"""check string for polyndromism"""
def check_input_string(word: str)-> str:
    check_string = ''.join(letter for letter in word if letter.isalnum())
    return check_string


def chek_word_polyndromism(word: str):
    if word[:] == word[::-1]:
        return print(f'Word {word} is polyndrom ')
    return print(f'Word {word} is not polyndrom ')


def main(word: str):
    """main controller"""
    check_str = check_input_string(word)
    chek_word_polyndromism(check_str)


if __name__ == '__main__':
    input_string = (input(' Enter word for chek polyndromism: ')).lower()
    main(input_string)
