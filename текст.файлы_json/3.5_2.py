from sys import stdin


def main():
    s = 0
    p = stdin.read().split("\n")
    for i in p:
        if i != "":
            h = i.split()
            s += int(h[2]) - int(h[1])
    print(round(s / (len(p) - 1)))


if __name__ == "__main__":
    main()