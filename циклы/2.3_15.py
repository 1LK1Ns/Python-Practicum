def main():
    n = int(input())
    c = 0
    for i in range(n):
        s = input()
        if 'зайка' in s:
            c += 1
    print(c)


if __name__ == '__main__':
    main()