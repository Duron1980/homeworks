def create_string() -> str:
    while True:
        string = input(' Enter a string up to 10 characters long - ')
        if len(string) > 10 or len(string) == 0:
            print(' You enter string wrong length ')
            continue
        break
    return string


def refactoring_string(STRING: str):
    if len(STRING) >= 5:
        modify_string = STRING[:len(STRING[:-3]) // 2] + STRING[-3:].lower() + STRING[len(STRING[:-3]) // 2:-3]
        print(modify_string)
    else:
        print('The rest of the line has no middle')


def main():
    string = create_string()
    refactoring_string(string)


if __name__ == '__main__':
    main()
