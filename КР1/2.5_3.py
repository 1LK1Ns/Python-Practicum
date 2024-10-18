def main():
    n = int(input())
    m = int(input())
    d = int(input())
    print(n, end='')
    for i in range(n + d, m + 1, d):
        print(f' - {i}', end='')
    for i in range(m, n - 1, -d):
        print(f' - {i}', end='')


if __name__ == '__main__':
    main()
