def task_1(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    # TODO
    return result


def fibonaci(N):
    if N < 2:
        return N
    return fibonaci(N - 1) + fibonaci(N - 2)


def task_2(N):
    # TODO
    return fibonaci(N - 1)


def task_3(N):
    result = []
    for i in range(1, N + 1):
        if N % i == 0:
            result.append(i)
    # TODO
    return result
