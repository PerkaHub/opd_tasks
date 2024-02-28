import math
def task_1(str):
    str = str.split('. ')
    str[-1] = str[-1][:-1]
    dict = {}
    for i in range(0, len(str)):
        dict[str[i]] = len(str[i].split())
    return dict
    print(task_1('First sent. Second sent and. Third sent and other.'))

def task_2(x1,y1,x2,y2):
    rastoyanie = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return rastoyanie
