def main():
    a = dict()
    while (s := input()) != "":
        w = s.split()
        for i in w:
            a[i[-1].upper()] = a.get(i[-1].upper(), []) + [i.lower()]
    for i, j in a.items():
        print(f"{i} - {", ".join(sorted(set(j)))}")


if __name__ == "__main__":
    main()