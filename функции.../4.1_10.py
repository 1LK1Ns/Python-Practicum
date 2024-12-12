def merge(a, b):
    c = list(a) + list(b)
    for i in range(len(c)):
        for j in range(len(c) - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]
    return tuple(c)
