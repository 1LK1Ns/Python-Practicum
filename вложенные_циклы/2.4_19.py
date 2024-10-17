def main():
    n = int(input())
    le = []
    lc = []
    c = n // 2 + n % 2
    for i in range(1, c + 1):
        li = []
        for j in range(1, n + 1):
            if len(li) == c:
                print(f'{li[n - j]:>{len(str(c))}}', end=' ')
                lc.append(li[n - j])
            else:
                print(f'{min(i, j):>{len(str(c))}}', end=' ')
                li.append(min(i, j))
                lc.append(min(i, j))
            if j == n:
                le.append(li)
        print()
    if n % 2 == 1:
        for i in range(n):
            lc.pop(-1)
    for i in range(n // 2):
        for j in range(n):
            print(f'{lc[-1]:>{len(str(c))}}', end=' ')
            lc.pop(-1)
        print()


if __name__ == '__main__':
    main()