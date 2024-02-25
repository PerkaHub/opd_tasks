# Пример 1
def task_1(n):

    i = 1
    x = 0
    while i <= n:
        x += 1/i
        i += 1
    return x


# Пример 2
def task_2(x, n):

    y = x
    i = 3
    while i <= n:
        y += x/i
        i += 2
    return y


# Пример 3
def task_3(n):

    i = 1
    y = 1
    while i <= n:
        y *= i
        i += 1
    return y


# Пример 4
def task_4(x, n):
    # TODO
    z = 1
    i = 2
    while i <= n:
        z *= (x + i) / i
        i += 1
    return z


# Пример 5
def task_5(x, n):
    # TODO
    y = 0
    i = 1
    while i <= n:
        y += (x*i) / (2*i)
        i += 1
    return y


# Пример 6
def task_6(n):
    # TODO
    z = 1
    i = 2
    while i <= n:
        z *= i
        i += 2
    return z