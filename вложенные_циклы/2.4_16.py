def main():
    n = int(input())
    w = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1:
                print(f'{i * j:^{w}}', end='')
            else:
                print(f'|{i * j:^{w}}', end='')
        print()
        if i != n:
            print('-' * (w * n + n - 1))


if __name__ == '__main__':
    main()