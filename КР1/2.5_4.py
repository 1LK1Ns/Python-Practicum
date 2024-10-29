def main():
    n = int(input())
    m = int(input())
    a = [int(input()) for _ in range(n)]
    print(max([a[i] for i in range(1, n - 1) if abs(a[i] - a[i - 1]) < m]))


if __name__ == '__main__':
    main()
