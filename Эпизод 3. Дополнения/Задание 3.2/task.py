def task_1(list_: list, num_):
    list_copy = list_.copy()
    start = 0
    end = len(list_copy)
    while start != end:
        middle = (start + end) // 2
        if list_copy[middle] == num_:
            start = middle
            break
        elif list_copy[middle] > num_:
            end = middle
        else:
            start = middle
    return str(start)


def task_2(num):
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True
