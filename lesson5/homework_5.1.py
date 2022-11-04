"""sort list by slice"""
from random import shuffle


def create_list() -> list:
    len_list = int(input(' Enter number elements of list: '))
    some_list = [el for el in range(len_list)]
    shuffle(some_list)
    print(some_list)
    return some_list


def sort_list(data_list: list, start_index: int, finish_index: int) -> list:
    sort_method = input(' Enter sort method direct/reverse: ')
    sorted_list = []
    sorted_list.extend(data_list[:start_index])
    sorted_list.extend(sorted(data_list[start_index:finish_index + 1])) if sort_method == 'direct' else sorted_list.extend(sorted(data_list[start_index:finish_index + 1], reverse=True))
    sorted_list.extend(data_list[finish_index + 1:])
    return sorted_list


def main():
    """main controller"""
    data_list = create_list()
    start_index = int(input(' Enter start index of sort '))
    finish_index = int(input(' Enter finish index of sort '))
    print(sort_list(data_list, start_index, finish_index))


if __name__ == '__main__':
    main()
