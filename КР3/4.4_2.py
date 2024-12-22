def add_number(number):
    n.append(number)


def get_sum():
    return " + ".join([str(i) for i in n]) + " = " + str(sum(n))


n = []