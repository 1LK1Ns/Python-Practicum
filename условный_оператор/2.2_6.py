def main():
    n = int(input())
    if n % 4 == 0:
        if n % 400 != 0 and n % 100 == 0:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()
