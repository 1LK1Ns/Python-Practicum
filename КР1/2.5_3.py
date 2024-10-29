def main():
    n = int(input())
    m = int(input())
    d = int(input())
    print(" - ".join([str(x) for x in range(n, m + 1, d)]), "-", " - ".join([str(y) for y in range(m, n - 1, -d)]))


if __name__ == '__main__':
    main()
