def main():
    f = []
    n = int(input())
    for i in range(n):
        s = input()
        f.append(s)
    s = input().upper()
    for i in f:
        if s in i.upper():
            print(i)


if __name__ == '__main__':
    main()