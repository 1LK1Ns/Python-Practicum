def main():
    n = int(input())
    c = 0
    for i in range(n):
        s = input()
        c += s.count('зайка')
    print(c)


if __name__ == '__main__':
    main()