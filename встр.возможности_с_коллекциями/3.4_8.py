from itertools import cycle, islice


def main():
    p = [input() for _ in range(int(input()))]
    for i in islice(cycle(p), 0, int(input())):
        print(i)


if __name__ == "__main__":
    main()