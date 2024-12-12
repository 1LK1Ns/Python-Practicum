def gcd(x, y):
    while x != y:
        x, y = max(x, y) - min(x, y), min(x, y)
    return x