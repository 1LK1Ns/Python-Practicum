def main():
    n = int(input())
    m = int(input())
    a = (n % 10 + m % 10) % 10 + (n // 10 % 10 + m // 10 % 10) % 10 * 10 + (n // 100 + m // 100) % 10 * 100
    print(a) 
if __name__ == '__main__':
    main()
