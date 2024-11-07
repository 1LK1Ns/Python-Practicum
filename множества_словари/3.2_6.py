def main():
    n = int(input())
    m = int(input())
    a = []
    for _ in range(n + m):
        if (x := input()) not in a:
            a.append(x)
        else:
            a.pop(a.index(x))
    if len(a) == 0:
        print("Таких нет")
    else:
        for i in sorted(a):
            print(i)


if __name__ == "__main__":
    main()