def main():
    a = set()
    while ((s := input().split()) != []):
        for i in range(len(s)):
            if s[i] == "зайка":
                a.add(s[i - 1] if i - 1 >= 0 else "")
                a.add(s[i + 1] if i + 1 <= len(s) - 1 else "")
    print("\n".join([i for i in a if i != ""]))


if __name__ == "__main__":
    main()