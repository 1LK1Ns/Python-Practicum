def main():
    n = int(input())
    m = int(input())
    c = 1
    le = len(str(n * m))
    for i in range(n):
        if (i + 1) % 2 == 1:
            for j in range(m):
                print(f'{c:>{le}}', end=' ')
                c += 1
            c -= 1
            print()
        else:
            for j in range(m):
                print(f'{m * (i + 1) - j:>{le}}', end=' ')
            c += m + 1
            print()


if __name__ == '__main__':
    main()
