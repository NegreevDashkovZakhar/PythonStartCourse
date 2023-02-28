# todo: replace this with an actual task
def task_1(str):
    words = str.split(' ')
    # TODO
    return len(words[-1])


def task_2(str):
    words = str.split(' ')
    result = ''
    for i in range(0, len(words) - 1, 2):
        (words[i + 1], words[i]) = (words[i], words[i + 1])
    for word in words:
        result += '{} '.format(word)
    # TODO
    return result[:-1]


def task_3(str):
    words = str.split(' ')
    result = 0

    for i in range(1, len(words)):
        if words[i][0] == words[i - 1][-1]:
            result += 1
    # TODO
    return result
