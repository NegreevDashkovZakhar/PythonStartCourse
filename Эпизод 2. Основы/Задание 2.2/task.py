import math


# Пример 1
def task_1(A):
    result = 0
    for num in A:
        if num > 0:
            result += num
    # TODO
    return result


# Пример 2
def task_2(A):
    sum = 0
    for num in A:
        sum += num
    # TODO
    return sum / len(A)


# Пример 3
def task_3(A):
    mean = task_2(A)
    sum = 0
    for num in A:
        sum += (num - mean) ** 2
    # TODO
    return math.sqrt(sum / len(A))
