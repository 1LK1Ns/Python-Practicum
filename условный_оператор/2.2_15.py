def main():
    a = int(input())
    b = int(input())
    n1 = a // 10
    n2 = a % 10
    n3 = b // 10
    n4 = b % 10
    m = max(n1, n2, n3, n4)
    mi = min(n1, n2, n3, n4)
    print(m * 100 + (n1 + n2 + n3 + n4 - m - mi) % 10 * 10 + mi)
if __name__ == '__main__':
    main()
