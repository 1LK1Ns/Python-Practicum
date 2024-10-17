def main():
    n = int(input())
    m = 0
    mi = 0
    for i in range(2, 11):
        ni = n
        s = 0
        while ni > 0:
            s += ni % i
            ni //= i
        if s > m:
            mi = i
            m = s
    print(mi)


if __name__ == '__main__':
    main()