# Пример 1
def task_1(n):
    i = 1
    result = 0
    while i <= 10:
        result += 1 / i
        i += 1
    # TODO
    return result


# Пример 2
def task_2(x, n):
    i = 1
    result = 0
    while i <= 17:
        result += x / i
        i += 2
    # TODO
    return result


# Пример 3
def task_3(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    # TODO
    return result


# Пример 4
def task_4(x, n):
    i = 2
    result = 1

    while i <= 9:
        result *= (x + i) / i
        i += 1
    # TODO
    return result


# Пример 5
def task_5(x, n):
    result = 0
    i = 1
    while i <= n:
        result += (x * i) / (2 * i)
        i += 1
    # TODO
    return result


# Пример 6
def task_6(n):
    i = 2
    result = 1
    while i <= 20:
        result *= i
        i += 2
    # TODO
    return result
