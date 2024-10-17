def main():
    n = int(input())
    c = 0
    for i in range(n):
        flag = False
        a = int(input())
        if a == 1:
            flag = True
        for i in range(2, int(a ** 0.5 + 1)):
            if a % i == 0:
                flag = True
                break
        if not flag:
            c += 1
    print(c)


if __name__ == '__main__':
    main()