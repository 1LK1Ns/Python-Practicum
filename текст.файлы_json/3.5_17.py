def main():
    s = ""
    with open("secret.txt", encoding="UTF-8") as f:
        t = f.read().rstrip("\n")
    for i in t:
        s += chr(ord(i) % 128)
    print(s)


if __name__ == "__main__":
    main()