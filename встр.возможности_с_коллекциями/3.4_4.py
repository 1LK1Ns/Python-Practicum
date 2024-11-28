from itertools import cycle


def main():
    s = ""
    n = input()
    for i in cycle(n.split()):
        s += f"{i} "
        if len(s) <= len(n) + 1:
            print(s)
        else:
            break


if __name__ == "__main__":
    main()