def main():
    n = set(int(i) for i in input().split("; "))
    d = {}
    for i in sorted(n):
        for j in sorted(n):
            a, b = int(i), int(j)
            while a != b:
                a, b = max(a, b) - min(a, b), min(a, b)
            if a == 1:
                d[i] = d.get(i, []) + [str(j)]
        if i not in d:
            continue
        print(f"{i} - {", ".join(d[i])}")


if __name__ == "__main__":
    main()