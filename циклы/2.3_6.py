def main():
    a = int(input())
    b = int(input())
    while a != b:
        a, b = max(a, b) - min(a, b), min(a, b)
    print(a)


if __name__ == '__main__':
    main()