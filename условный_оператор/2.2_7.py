def main():
    n = int(input())
    if (n % 100 == n // 100 % 10 * 10 + n // 1000):
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()
