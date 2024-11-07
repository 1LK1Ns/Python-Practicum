def main():
    a = []
    for _ in range(int(input())):
        s = input().split()
        for i in set("".join(s[1:]).split(",")):
            a.append(i)
    a = [i for i in a if a.count(i) == 1]
    for i in sorted(a):
        print(i)


if __name__ == "__main__":
    main()