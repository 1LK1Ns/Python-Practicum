def main():
    n = int(input())
    m = int(input())
    a = set()
    for _ in range(n + m):
        if (x := input()) not in a:
            a.add(x)
        else:
            a.discard(x)
    print("Таких нет" if len(a) == 0 else len(a))


if __name__ == "__main__":
    main()