def gcd(*num):
    a = int(num[0])
    for i in range(1, len(num)):
        b = int(num[i])
        while a != b:
            a, b = max(a, b) - min(a, b), min(a, b)
    return a