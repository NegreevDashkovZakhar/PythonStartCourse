def task_1(str):
    letters_dict = {}
    letters_set = set(str)
    for letter in letters_set:
        if letter == ' ' or letter.isnumeric():
            continue
        letters_dict[letter] = 0
    for letter in str:
        if letter == ' ' or letter.isnumeric():
            continue
        letters_dict[letter] = letters_dict[letter] + 1
    # TODO
    return letters_dict


def task_2(list):
    numbers = set(list)
    result = 0
    for num in numbers:
        result += num
    # TODO
    return result


def task_3(cities):
    # TODO
    return '{}.'.format(', '.join(cities))


def task_4(a, b):
    a_set = set(a)
    b_set = set(b)
    # TODO
    return list(a_set & b_set)
