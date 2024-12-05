def main():
    n = int(input())
    s = ""
    with open("public.txt", encoding="UTF-8") as f:
        t = f.read().rstrip("\n")
    for i in t:
        c = ord(i) + n
        if 65 <= ord(i) <= 90:
            while c > 90:
                c -= 26
            while c < 65:
                c += 26
            s += chr(c)
        elif 97 <= ord(i) <= 122:
            while c > 122:
                c -= 26
            while c < 97:
                c += 26
            s += chr(c)
        else:
            s += i
    with open("private.txt", "w", encoding="UTF-8") as f:
        f.write(s)


if __name__ == "__main__":
    main()