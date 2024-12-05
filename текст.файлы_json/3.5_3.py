from sys import stdin


def main():
    text = stdin.read().split("\n")
    out = []
    for i in text:
        if "#" in i:
            out.append(i[:i.index("#")])
        else:
            out.append(i)
    for i in out:
        if i != "":
            print(i)


if __name__ == "__main__":
    main()