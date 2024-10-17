def main():
    L = int(input())
    n = int(input())
    d = 0
    ss = ''
    for i in range(n):
        s = input()
        if len(s) < L - d:
            ss += f'{s}\n'
            d += len(s)
        else:
            if L - d > 3:
                ss += f'{s[:L - d - 3]}...'
                break
            else:
                ss = f'{ss[:-((2 + ss.count('\n')) - (L - d))]}...'
                break
    print(ss)


if __name__ == '__main__':
    main()