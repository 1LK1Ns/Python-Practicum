def main():
    a = dict()
    for _ in range(int(input())):
        s = input()
        a[s] = a.get(s, 0) + 1
    print(sum([a[i] for i in a if a[i] != 1]))


if __name__ == "__main__":
    main()