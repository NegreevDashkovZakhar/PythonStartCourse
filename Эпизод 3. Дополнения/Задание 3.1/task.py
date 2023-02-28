import math


def task_1(text: str):
    text=text[:-1]
    result = {}
    sentences = text.split('. ')
    for sentence in sentences:
        result[sentence] = len(sentence.split(' '))
    return result


def task_2(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
