def main():
    n = int(input())
    a = n // 100 % 10 * 1000 + n // 1000 * 100 + n % 10 * 10 + n % 100 // 10
    print(a)
if __name__ == '__main__':
    main()
