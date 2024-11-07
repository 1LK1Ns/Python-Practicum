def main():
    a = dict()
    for i in range(int(input())):
        for j in range(len(s := input().split()) - 1):
            a[s[j + 1]] = a.get(s[j + 1], []) + [s[0]]
    if (d := input()) in a:
        print("\n".join(sorted(a.get(d))))
    else:
        print("Таких нет")


if __name__ == "__main__":
    main()