import math
# Пример 1
def task_1(A):
    # TODO
    sum = 0
    for i in A:
        if i > 0:
            sum += i
    return sum


# Пример 2
def task_2(A):
    # TODO
    sr = 0
    k = 0
    for i in A:
        sr += i
        k += 1
    sr = sr / k
    return sr


# Пример 3
def task_3(A):
    # TODO
    sum = 0
    x = 0
    for i in A:
        x += i / len(A)
    for i in A:
        sum += (i - x) ** 2
    return math.sqrt(sum / len(A))
