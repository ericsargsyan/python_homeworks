# 1. Write a Python program to create a dictionary from a string.
def create_dict(string: str):
    str_dict = {}
    for i, j in enumerate(string):
        str_dict.update({j: i})
    return str_dict


# 2. Write a Python program to print a dictionary in a tab form.
def show_dict(dictionary: dict):
    for k, v in dictionary.items():
        print(k, '\t', v)


# 3. Write a Python program to check if value exists in a dictionary.
def exists(dictionary: dict, value: str):
    return value in dictionary.values()


# 4․ Write a Python program to remove duplicate values from Dictionary.
def remove_duplicates(dictionary: dict):
    without_copies = {}
    # without_copies.update({i: dictionary[i] for i in dictionary if dictionary[i] not in without_copies.values()})
    # without_copies = {i: dictionary[i] for i in dictionary if dictionary[i] not in without_copies.values()}
    for i in dictionary:
        if dictionary[i] not in without_copies.values():
            without_copies.update({i: dictionary[i]})
    print(without_copies)


# 5. Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x).
def dict_exp():
    n = int(input("Input number of elements: "))
    dict_n = {i: i ** 2 for i in range(1, n + 1)}
    return dict_n


# 6. Write a Python script to merge two Python dictionaries
def merge_dict(dict1: dict, dict2: dict):
    dict1.update(dict2)
    return dict1


# 7. Write a Python program to sum all the items in a dictionary
def sum_dict(dictionary: dict):
    sum_ = 0
    for i in dictionary:
        if type(dictionary[i]) is int:
            sum_ += dictionary[i]
    return sum_


# 8. Write a Python program to remove a key from a dictionary
def remove_key(dictionary: dict, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary


# 9. Write a Python program to map two lists into a dictionary
def map_list(list1: list, list2: list):
    dictionary = {}
    # dictionary = dict(zip(list1, list2))
    for i in range(len(list1)):
        dictionary.update({list1[i]: list2[i]})
    return dictionary


# 10. Write a Python program to get the maximum and minimum value in a dictionary
def min_max(dictionary: dict):
    max_v = 0
    min_v = 0
    for i in dictionary:
        for j in dictionary:
            if dictionary[i] < dictionary[j]:
                max_v = dictionary[j]
            if dictionary[i] > dictionary[j]:
                min_v = dictionary[j]
    return max_v, min_v


# 11. Write a Python program to check a dictionary is empty or not
def isempty(dictionary):
    if dictionary:
        return False
    return True


# 12. Write a Python program to combine two dictionary adding values for common keys
def common_dict(dict1: dict, dict2: dict):
    dictionary = {}
    for i in dict1, dict2:
        dictionary.update(i)
    return dictionary


# 13. Write a Python program to print all unique values in a dictionary
def unique_values(dictionary: dict):
    ls = []
    for i in dictionary:
        if dictionary[i] not in ls:
            ls.append(dictionary[i])
    return ls


# 14. Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary


# 15. Write a Python program to drop empty Items from a given Dictionary
def drop_empty(dictionary: dict):
    new_dict = {k: v for k, v in dictionary.items() if v is not None}
    return new_dict


# 16. Sort Dictionary by keys in ascending(descending) order
def sort_ascending_k(dictionary: dict):
    ls = list(dictionary.items())
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][0] < ls[j][0]:
                ls[i], ls[j] = ls[j], ls[i]
    dictionary = dict(ls)
    return dictionary


def sort_descending_k(dictionary: dict):
    ls = list(dictionary.items())
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][1] > ls[j][1]:
                ls[i], ls[j] = ls[j], ls[i]
    dictionary = dict(ls)
    return dictionary


#17. Sort Dictionary by values in ascending(descending) order
def sort_ascending_v(dictionary: dict):
    # dictionary = sorted(dictionary.keys())
    ls = list(dictionary.items())
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][1] < ls[j][1]:
                ls[i], ls[j] = ls[j], ls[i]
    dictionary = dict(ls)
    return dictionary


def sort_descending_v(dictionary: dict):
    # dictionary = sorted(dictionary.keys())
    ls = list(dictionary.items())
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][1] > ls[j][1]:
                ls[i], ls[j] = ls[j], ls[i]
    dictionary = dict(ls)
    return dictionary


# 18. Write a python program to remove spaces in dictionary keys and values.
def rm_spaces(dictionary: dict):
    # for k, v in dictionary.items():
    #     if type(k) == str:
    dictionary = {k.replace(' ',''): v.replace(' ','')
                  for k, v in dictionary.items() if type(k) == str and type(v) == str}
        # if type(v) == str:
        #     dictionary = {k: v.replace(' ','') for k, v in dictionary.items()}
    print(dictionary)


# 19. Find N most frequent words in text sequence, collecting data in a dictionary.
def validation(text: str) -> str:
    for i in text:
        if ord(i) in range(33, 65) or ord(i) \
                in range(91, 97) or ord(i) in range(123, 127):
            text = text.replace(i, '')
    return text


def frequent_words(text: str, n: int):
    validation(text)
    ls_text = text.split()
    dict_text = {}
    for i in ls_text:
        dict_text[i] = 0
    for i in ls_text:
        if i in dict_text.keys():
            dict_text[i] += 1
    dict_text = {i: dict_text[i] for i in sorted(dict_text, key=lambda k: dict_text[k], reverse=True)}
    a = list(dict_text.items())
    for i in range(n):
        print(f"\t'{a[i][0]}'\t-->\t'{a[i][1]}'")
