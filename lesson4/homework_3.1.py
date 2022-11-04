from random import shuffle


def sort_list(my_list: list):
    finish_list = []
    step = 5
    for i in range(0, len(my_list), step):
        if i % 2 == 0:
            finish_list.extend(sorted(my_list[i: i + step]))
        else:
            finish_list.extend(sorted(my_list[i: i + step], reverse=True))
    print('Result list ', finish_list)


def main(number: int):
    my_list = list(range(1, number + 1))
    shuffle(my_list)
    print('Original list -  ', my_list)
    sort_list(my_list)


if __name__ == '__main__':
    number_elements = int(input(' Enter number elements of list - '))
    main(number_elements)
