def main():
    n = int(input())
    m = 'яя'
    for i in range(n):
        s = input()
        if s < m:
            m = s
    print(m)


if __name__ == '__main__':
    main()