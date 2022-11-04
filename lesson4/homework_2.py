def fizzbuzz(fizz: int, buzz: int, converted_number: int) -> print:
    return print(*(
        'FB' if value % fizz == 0 and value % buzz == 0 else 'F' if value % fizz == 0 else 'B' if value % buzz == 0 else value
        for value in range(1, converted_number + 1)))


def main(file_name: str):
    with open(file_name, 'r') as file:
        for line in file:
            fizz, buzz, converted_number = line.split()
            fizzbuzz(int(fizz), int(buzz), int(converted_number))


if __name__ == '__main__':
    file_name = 'file_1.txt'
    main(file_name)
