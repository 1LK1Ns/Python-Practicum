def main():
    n = int(input())
    se = 0
    s = 2
    while se < n:
        se = (s * (s + 1)) // 2
        s += 1
    s -= 2
    s1 = (s * (s + 1)) // 2 + 1
    le = -1
    for i in range(s1, n + 1):
        le += len(str(i)) + 1
    print(f'{1:^{le}}')
    c = 2
    s = 2
    while c <= n:
        a = ''
        se = (s * (s + 1)) // 2
        while c <= se:
            if c <= n:
                a += str(c) + ' '
            c += 1
        print(f'{a:^{le + 1}}')
        s += 1


if __name__ == '__main__':
    main()