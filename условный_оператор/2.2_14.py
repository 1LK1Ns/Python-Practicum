def main():
    n = int(input())
    n1 = max(n // 100, n // 10 % 10, n % 10)
    n2 = min(n // 100, n // 10 % 10, n % 10)
    n3 = n // 100 + n // 10 % 10 + n % 10 - n1 - n2
    if n2 == 0:
        print(str(n3) + str(n2), str(n1) + str(n3))
    else:
        print(str(n2) + str(n3), str(n1) + str(n3))
if __name__ == '__main__':
    main()
