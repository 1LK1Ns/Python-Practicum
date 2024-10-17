def main():
    n = int(input())
    f = True
    for i in range(n):
        s = input()
        if s[0] not in 'абв':
            f = False
            break
    if f:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()