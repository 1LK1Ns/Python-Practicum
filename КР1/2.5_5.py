def main():
    n = int(input())
    minn = 1e9
    for i in range(n):
        s = input()
        c = 0
        summ = 0
        while s != 'end':
            summ += int(s)
            c += 1
            s = input()
        if summ / c < minn:
            minn = summ / c
    print(f'{minn:.2f}')


if __name__ == '__main__':
    main()
