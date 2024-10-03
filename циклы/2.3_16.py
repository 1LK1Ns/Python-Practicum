def main():
    n = input()
    f = 0
    for i in range(len(n)):
        if n[i] != n[-i - 1]:
            print('NO')
            f = 1
            break
    if f == 0:
        print('YES')


if __name__ == '__main__':
    main()
