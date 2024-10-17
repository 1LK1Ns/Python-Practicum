def main():
    s = input().lower().split()
    if ''.join(s) == ''.join(s)[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()