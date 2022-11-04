from random import shuffle


def elements_with_even_indices(origin_list: list):
    print('1).Elements_with_even_indices - ', origin_list[2::2])


def sum_elemets(origin_list: list):
    print('2).Sum elements of list - ', sum(origin_list))


def sum_even_notiven_elements(origin_list: list):
    sum_even_elemets = []
    sum_noteven_elemets = []
    [sum_even_elemets.append(element) if (element % 2 == 0) else sum_noteven_elemets.append(
        element) if element % 2 != 0 else 0 for element in origin_list]
    print('3).Even elements - ', sum_even_elemets)
    print('4).Not even elements - ', sum_noteven_elemets)

def max_element(origin_list: list):
    max_el = max(origin_list)
    index_max_el = origin_list.index(max_el)
    print('5).Max element - ', max_el)
    print('6).Index max element - ', index_max_el)



def main(number: int):
    my_list = list(range(1,number+1))
    shuffle(my_list)
    print('Original list -  ', my_list)
    elements_with_even_indices(my_list)
    sum_elemets(my_list)
    sum_even_notiven_elements(my_list)
    max_element(my_list)



if __name__ == '__main__':
    number_elements = int(input(' Enter number elements of list - '))
    main(number_elements)
