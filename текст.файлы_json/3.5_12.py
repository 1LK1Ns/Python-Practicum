def main():
    with open(input(), encoding="UTF-8") as f:
        t = f.read().split("\n")
    even = [[] for _ in range(len(t) - 1)]
    odd = [[] for _ in range(len(t) - 1)]
    eq = [[] for _ in range(len(t) - 1)]
    for i in range(len(t) - 1):
        num = t[i].split()
        for j in num:
            e = [k for k in j if int(k) % 2 == 0]
            o = [k for k in j if int(k) % 2 != 0]
            if len(e) > len(o):
                even[i].append(j)
            elif len(o) > len(e):
                odd[i].append(j)
            else:
                eq[i].append(j)
    even = "\n".join([" ".join(i) for i in even]) + "\n"
    odd = "\n".join([" ".join(i) for i in odd]) + "\n"
    eq = "\n".join([" ".join(i) for i in eq]) + "\n"
    with open(input(), "w", encoding="UTF-8") as f:
        f.write(even)
    with open(input(), "w", encoding="UTF-8") as f:
        f.write(odd)
    with open(input(), "w", encoding="UTF-8") as f:
        f.write(eq)


if __name__ == "__main__":
    main()