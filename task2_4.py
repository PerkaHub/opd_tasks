def task_1(str):
    # TODO
    str1 = set()
    a = {}
    for i in str:
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            str1.add(i)
            a[i] = str.count(i)
    return a


def task_2(list):
    # TODO
    return sum(set(list))


def task_3(cities):
    # TODO
    str = ", ".join(cities) + "."
    return str


def task_4(a, b):
    # TODO
    a = set(a) & set(b)
    return list(a)
