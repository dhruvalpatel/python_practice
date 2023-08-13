"""Sort a list without using the keyword Sort."""


def sort_list(my_list):
    """
    This technic is known as the bubble sort.
    Where you compare each element with other elements to perform sorting.
    """
    sorted_list = []
    while my_list:
        min = my_list[0]
        for x in my_list:
            if x < min:
                min = x
        sorted_list.append(min)
        my_list.remove(min)
    print(sorted_list)


my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
sort_list(my_list)
