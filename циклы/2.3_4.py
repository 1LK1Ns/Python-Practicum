def main():
    k = int(input())
    n = int(input())
    if k < n:
        for i in range(k, n + 1):
            print(i, end=' ')
    else:
        for i in range(k, n - 1, -1):
            print(i, end=' ')


if __name__ == '__main__':
    main()
