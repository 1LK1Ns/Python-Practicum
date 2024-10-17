def main():
    n = int(input())
    a = 0
    for i in range(n):
        f = False
        while (s := input()) != 'ВСЁ':
            if s == 'зайка':
                f = True
        if f:
            a += 1
    print(a)


if __name__ == '__main__':
    main()