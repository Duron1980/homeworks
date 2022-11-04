def main(fizz: int, buzz: int, converted_number: int):
    return print(*('FB' if value % fizz == 0 and value % buzz == 0 else 'F' if value % fizz == 0 else 'B' if value % buzz == 0 else value for value in range(1, converted_number+1)))

if __name__ == '__main__':
    fizz = int(input(' Enter fizz number please- '))
    buzz = int(input(' Enter buzz number please- '))
    converted_number = int(input(' Enter converted number please- '))
    main(fizz, buzz, converted_number)