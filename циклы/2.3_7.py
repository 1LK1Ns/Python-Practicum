def main():
    a = int(input())
    b = int(input())
    p = a * b
    while a != b:
        a, b = max(a, b) - min(a, b), min(a, b)
    print(int(p / a))


if __name__ == '__main__':
    main()