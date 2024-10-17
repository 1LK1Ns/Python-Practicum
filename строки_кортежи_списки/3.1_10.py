def main():
    s = ''.join(input().lower().split())
    ss = ''
    while s != 'финиш':
        ss += s
        s = ''.join(input().lower().split())
    ss = sorted(ss)
    maxx = 0
    c = 1
    a = 'я'
    for i in range(len(ss) - 1):
        if ss[i + 1] == ss[i]:
            c += 1
        else:
            if c > maxx:
                maxx = c
                a = ss[i]
            c = 1
    print(a)


if __name__ == '__main__':
    main()