# todo: replace this with an actual task
def task_1(str):
    # TODO
    k = 0
    for i in str:
        if i == " ":
            k = 0
        else:
            k += 1
    return k


def task_2(str):
    # TODO
    arr = str.split()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return " ".join(arr)


def task_3(str):
    # TODO
    k = 0

    for i in range(0,len(str)):
        if str[i] == " ":
            if str[i-1] == str[i+1]:
                k += 1
    return k
