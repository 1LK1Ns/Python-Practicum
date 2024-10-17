def main():
    n = int(input())
    s = 0
    for i in range(n):
        a = input()
        for j in a:
            s += int(j)
    print(s)


if __name__ == '__main__':
    main()