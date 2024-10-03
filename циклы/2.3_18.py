def main():
    n = int(input())
    s = ''
    while n > 1:
        for i in range(2, int(n) + 1):
            if n % i == 0:
                s += f'{i} * '
                n /= i
                break
    print(s[:-3])


if __name__ == '__main__':
    main()