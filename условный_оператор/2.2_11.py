def main():
    n = int(input())
    n1 = n % 10
    n2 = n // 10 % 10
    n3 = n // 100
    if max(n1, n2, n3) + min(n1, n2, n3) == (n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3)) * 2:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()
