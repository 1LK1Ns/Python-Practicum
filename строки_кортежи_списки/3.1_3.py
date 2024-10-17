def main():
    L = int(input())
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) > L:
            print(f'{s[:L - 3]}...')
        else:
            print(s)


if __name__ == '__main__':
    main()