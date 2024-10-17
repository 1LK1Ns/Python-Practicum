def main():
    n = int(input())
    m = int(input())
    c = 1
    le = len(str(n * m))
    for i in range(n):
        for j in range(m):
            print(f'{c:>{le}}', end=' ')
            c += 1
        print()


if __name__ == '__main__':
    main()