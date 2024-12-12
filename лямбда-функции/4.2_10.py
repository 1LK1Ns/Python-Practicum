def secret_replace(text, **replaces):
    res = ""
    c = {k: (v, 0) for k, v in replaces.items()}
    for i in text:
        if i in c:
            res += c[i][0][c[i][1]]
            c[i] = c[i][0], (c[i][1] + 1) % len(c[i][0])
        else:
            res += i
    return res