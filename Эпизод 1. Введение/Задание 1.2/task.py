from math import sqrt, log, tan, cos, log10


# Пример 1
def task_1(a, b):
    if a > b:
        return sqrt(a * b) - 3
    elif a == b:
        return log10(2)
    # TODO
    return log(a ** 3 + 1) / b


# Пример 2
def task_2(a, b):
    if a < b:
        return tan(a / b) + 1
    elif a == b:
        return tan(-1)
    # TODO
    return sqrt(a * b - 5) / a


# Пример 3
def task_3(a, b):
    if a > b:
        return log10(a * b) + 21
    elif a == b:
        return tan(-5)
    # TODO
    return log(3 * a / b) + 1


# Пример 4
def task_4(a, b):
    if a > b:
        return sqrt(a * b - 1)
    elif a == b:
        return log10(255)
    # TODO
    return tan(a - 5) / b


# Пример 5
def task_5(a, b):
    if a > b:
        return log(a / b) + 31
    elif a == b:
        return tan(-25)
    # TODO
    return cos(a * 5 - 1) / a


# Пример 6
def task_6(a, b):
    if a < b:
        return sqrt(b / a + 1)
    elif a == b:
        return sqrt(25)
    # TODO
    return log10(a ** 3 - 5) / b
