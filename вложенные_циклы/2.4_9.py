def main():
    n = int(input())
    s = ''
    for i in range(n):
        a = input()
        m = 0
        for j in a:
            if int(j) > m:
                m = int(j)
        s += str(m)
    print(s)


if __name__ == '__main__':
    main()