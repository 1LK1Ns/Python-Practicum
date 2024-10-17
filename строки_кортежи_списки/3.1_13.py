def main():
    num = []
    n = int(input())
    for i in range(n):
        a = int(input())
        num.append(a)
    a = int(input())
    for i in num:
        print(i ** a)


if __name__ == '__main__':
    main()