def main():
    n = int(input())
    c = 1
    k = 1
    while c <= n:
        for j in range(k):
            if c <= n:
                print(c, end=' ')
                c += 1
        k += 1
        print()


if __name__ == '__main__':
    main()