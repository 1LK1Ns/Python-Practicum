def modern_print(n):
    global s
    if n not in s:
        s += [n]
        print(n)


s = []