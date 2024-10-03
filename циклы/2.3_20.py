def main():
    n = int(input())
    hn0 = 0
    a = -1
    for i in range(n):
        b = int(input())
        h = b % 256
        r = b // 256 % 256
        m = b // 256 ** 2
        hn = (37 * (m + r + hn0)) % 256
        if hn != h or h >= 100:
            a = i
            break
        hn0 = h
    print(a)


if __name__ == '__main__':
    main()