def create_string() -> str:
    while True:
        string = input(' Enter a string with a length of 5 to 15 characters - ')
        if 5 > len(string) or len(string) > 15:
            print(' You enter string wrong length ')
            continue
        break
    return string


def refactoring_string(string: str) -> print:
    modify_string = (string[len(string) // 2:] + string[:len(string) // 2])[:-3] +  (string[len(string) // 2:] + string[:len(string) // 2])[-3:].upper()
    print(modify_string)

def main():
    string = create_string()
    refactoring_string(string)


if __name__ == '__main__':
    main()
