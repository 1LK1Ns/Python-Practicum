def main():
    num = input().split()
    a = int(num[0])
    for i in range(1, len(num)):
        b = int(num[i])
        while a != b:
            a, b = max(a, b) - min(a, b), min(a, b)
    print(a)


if __name__ == '__main__':
    main()