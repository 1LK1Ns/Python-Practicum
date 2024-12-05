from sys import stdin


def main():
    t = input().lower()
    text = stdin.read().split("\n")
    c = 0
    for i in text:
        with open(i, encoding="UTF-8") as f:
            p = " ".join(f.read().split("\n")).lower()
        s = ""
        for j in range(len(p) - 1):
            fl = 1
            if p[j] == " " and p[j + 1] == " ":
                fl = 0
            if fl == 1:
                s += p[j]
        if t in s:
            print(i)
            c = 1
    if c == 0:
        print("404. Not Found")


if __name__ == "__main__":
    main()