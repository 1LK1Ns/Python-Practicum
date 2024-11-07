def main():
    a = {}
    for _ in range(int(input())):
        x, y = map(int, input().split())
        x //= 10
        y //= 10
        a[(x, y)] = a.get((x, y), 0) + 1
    print(max(a.values()))


if __name__ == "__main__":
    main()