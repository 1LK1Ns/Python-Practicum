def main():
    n = int(input())
    a = int(input())
    for i in range(n - 1):
        b = int(input())
        while a != b:
            a, b = max(a, b) - min(a, b), min(a, b)
    print(a)


if __name__ == '__main__':
    main()