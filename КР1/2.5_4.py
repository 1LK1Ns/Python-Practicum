def main():
    n = int(input())
    m = int(input())
    a1 = int(input())
    maxx = -1e9
    for i in range(n - 1):
        a2 = int(input())
        if abs(a2 - a1) < m:
            if a2 > maxx:
                maxx = a2
        a1 = a2
    print(maxx)


if __name__ == '__main__':
    main()
