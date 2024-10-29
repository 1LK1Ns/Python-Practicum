def main():
    n = int(input())
    minn = 1e9
    for i in range(n):
        s = input()
        a = []
        while s != 'end':
            a.append(int(s))
            s = input()
        minn = min(minn, sum(a) / len(a))
    print(f'{minn:.2f}')


if __name__ == '__main__':
    main()
