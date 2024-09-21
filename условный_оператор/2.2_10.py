def main():
    n = int(input())
    s1 = n % 10 + n // 10 % 10
    s2 = n // 10 % 10 + n // 100
    print(str(max(s1, s2)) + str(min(s1, s2)))
if __name__ == '__main__':
    main()
