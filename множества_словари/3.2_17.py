def main():
    d = dict()
    while (s := input().split()) != []:
        d[s[0]] = d.get(s[0], []) + [s[1]]
        d[s[1]] = d.get(s[1], []) + [s[0]]
    for k, v in sorted(d.items()):
        a = []
        for i in range(len(v)):
            a += d[v[i]]
        a = set(a)
        a.discard(k)
        for i in d[k]:
            a.discard(i)
        print(f"{k}: {", ".join(sorted(a))}")


if __name__ == "__main__":
    main()