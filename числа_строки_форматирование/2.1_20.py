def main():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    c1 = (m * n - k2 * n) // (k1 - k2)
    c2 = n - c1
    print(c1, c2)
if __name__ == '__main__':
    main()
