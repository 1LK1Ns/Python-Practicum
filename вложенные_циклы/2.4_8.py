def main():
    n = int(input())
    m = 0
    for i in range(n):
        s = 0
        p = input()
        a = input()
        for j in a:
            s += int(j)
        if s >= m:
            m = s
            w = p
    print(w)


if __name__ == '__main__':
    main()