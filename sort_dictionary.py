"""Sort a dictionary / dict comprehension"""


def sort_dict_by_key_method_1(input_dict):
    """Sort Dictionary By Key"""
    keys = list(input_dict.keys())
    sorted_keys = keys
    sorted_dict = {}
    for i in sorted_keys:
        sorted_dict[i] = input_dict[i]
    print("sort_dict_by_key_method_1: ", sorted_dict)


def sort_dict_by_key_method_2(input_dict):
    """Sort Dictionary By Key with lexicographical order."""
    from collections import OrderedDict
    order_dict = OrderedDict(sorted(input_dict.items()))
    print("sort_dict_by_key_method_2: ", order_dict)


def sort_dict_by_key_method_3(input_dict):
    """Sort Dictionary By Key using sorted"""
    sorted_dict = dict(sorted(input_dict.items()))
    print("sort_dict_by_key_method_3: ", sorted_dict)


def sort_dict_by_value_method_1(input_dict):
    """Sort Dictionary By value"""
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))  # key= index from (key, value) to sort
    print("sort_dict_by_key_method_3: ", sorted_dict)


my_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# By key
sort_dict_by_key_method_1(my_dict)
sort_dict_by_key_method_2(my_dict)
sort_dict_by_key_method_3(my_dict)
# By value
sort_dict_by_value_method_1(my_dict)

