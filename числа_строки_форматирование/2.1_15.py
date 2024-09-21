def main():
    n = int(input())
    m = int(input())
    t = int(input())
    m += t % 60
    n += m // 60 + t // 60
    m %= 60
    n %= 24
    print(f"{n:0>2}:{m:0>2}")
if __name__ == '__main__':
    main()
