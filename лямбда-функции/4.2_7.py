def enter_results(*n):
    global l1, l2
    l1 += n[0::2]
    l2 += n[1::2]


def get_sum():
    global l1, l2
    return round(sum(l1), 2), round(sum(l2), 2)


def get_average():
    global l1, l2
    return round(sum(l1) / len(l1), 2), round(sum(l2) / len(l2), 2)


l1 = []
l2 = []