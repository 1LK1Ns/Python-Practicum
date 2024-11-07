def main():
    a = []
    for i in (input().split()):
        i = bin(int(i))[2:]
        s = dict()
        s["digits"] = len(i)
        s["units"] = i.count("1")
        s["zeros"] = i.count("0")
        a.append(s)
    print(a)


if __name__ == "__main__":
    main()