def main():
    for _ in range(int(input())):
        s = input()
        a = int(s[:s.index("&")])
        s = s[s.index("&") + 1:]
        b = int(s[:s.index("&")])
        s = s[s.index("&") + 1:]
        print(s[a::2][:b])


if __name__ == "__main__":
    main()