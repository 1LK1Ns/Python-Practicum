def main():
    n = int(input())
    m = int(input())
    c = 1
    le = len(str(n * m))
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                print(f'{c + n * j:>{le}}', end=' ')
            else:
                print(f'{n * (j + 1) - i:>{le}}', end=' ')
        c += 1
        print()


if __name__ == '__main__':
    main()
