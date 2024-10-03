def main():
    n = int(input())
    f = 0
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            f = 1
            break
    if f == 1 or n == 1:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()