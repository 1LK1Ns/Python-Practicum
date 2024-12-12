def can_eat(h, f):
    if (abs(f[0] - h[0]) == 2 and abs(f[1] - h[1]) == 1) or \
       (abs(f[0] - h[0]) == 1 and abs(f[1] - h[1]) == 2):
        return True
    return False