def main():
    num = input().split()
    n = int(input())
    for i in range(len(num)):
        num[i] = str(int(num[i]) ** n)
    print(' '.join(num))


if __name__ == '__main__':
    main()