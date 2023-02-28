from math import sqrt


def task_1(list_: list):
    items_set = set(list_)
    max_occ = 0
    max_val = -1
    for item in items_set:
        occ = list_.count(item)
        if occ > max_occ:
            max_occ = occ
            max_val = item
    return max_val


def task_2(x_, y_):
    count = len(x_)
    x_set = set(x_)
    y_set = set(y_)
    diffs = []
    sums = []
    for i in range(0, count):
        diffs.append(x_[i] - y_[i])
        sums.append(x_[i] + y_[i])
    diffs_set = set(diffs)
    sums_set = set(sums)
    can_capture = len(x_set) != count or len(y_set) != count or len(diffs_set) != count or len(sums_set) != count
    print(can_capture)
    return 'YES' if can_capture else 'NO'


def dist(x, y, xs, ys):
    return sqrt((x - xs) ** 2 + (y - ys) ** 2)


def task_3(x, y, xc, yc, r):
    return dist(x, y, xc, yc) <= r


def task_4(list_: list):
    result = 0
    for i in range(1, len(list_) - 1):
        if list_[i] > list_[i - 1] and list_[i] > list_[i + 1]:
            result += 1
    return result


def task_5(a):
    f = open('file.txt', 'r')
    text = f.read()
    f.close()
    text = text.lower()
    result = []
    rows = text.split('\n')
    for row in rows:
        if row == '':
            continue
        new_row = ''
        for i in range(0, len(row)):
            if row[i] == ' ':
                new_row += 'b'
                continue
            new_row += chr((ord(row[i]) + a - 97) % 26 + 97)
        result.append(new_row)
    return result
