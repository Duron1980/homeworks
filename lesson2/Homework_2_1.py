def main(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return print(f'{year} year is leap ')
    return print(f'{year} year is not leap ')

if __name__ == '__main__':
    year = int(input(' Enter year please- '))
    main(year)