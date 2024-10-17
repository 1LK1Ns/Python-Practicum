def main():
    n = int(input())
    c = 0
    for i in range(n):
        a = input()
        flag = False
        for j in range(len(a)):
            if a[j] != a[-j - 1]:
                flag = True
                break
        if not flag:
            c += 1
    print(c)


if __name__ == '__main__':
    main()