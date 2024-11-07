def main():
    d = dict()
    while (s := input().split()) != []:
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
    for k, v in d.items():
        print(k, v)


if __name__ == "__main__":
    main()