def main():
    a = dict()
    s = input()
    while s != "":
        w = s.split()
        for i in w:
            a[i[-1].upper()] = a.get(i[-1].upper(), []) + [i.lower()]
        s = input()
    for i, j in a.items():
        print(f"{i} - {", ".join(sorted(set(j)))}")


if __name__ == "__main__":
    main()