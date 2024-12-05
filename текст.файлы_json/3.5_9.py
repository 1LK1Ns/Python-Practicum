def main():
    s = ""
    with open(input(), encoding="UTF-8") as f:
        t = f.read()
    t = t.replace("\t", "")
    for i in range(len(t) - 1):
        fl = 1
        if ((t[i] == " " and t[i + 1] == " ") or (t[i] == "\n" and t[i + 1] == "\n")
           or (t[i] == " " and t[i + 1] == '\n')):
            fl = 0
        if fl == 1:
            s += t[i]
    s = s.replace("\n ", "\n")
    if s[0] == " ":
        s = s[1:]
    if s[-1] == " ":
        s = s[:-1]
    with open(input(), "w", encoding="UTF-8") as f:
        f.write(s)


if __name__ == "__main__":
    main()