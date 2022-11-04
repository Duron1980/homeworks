def main(year: int):
    print(f'{year} year is leap ' if not year % 4 and year % 100 or not year % 400 else f'{year} year is not leap ')
    return

if __name__ == '__main__':
    year = int(input(' Enter year please- '))
    main(year)