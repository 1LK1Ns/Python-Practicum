from sys import stdin


def main():
    numb = " ".join(stdin.read().split("\n")).split()
    print(sum([int(i) for i in numb]))


if __name__ == "__main__":
    main()