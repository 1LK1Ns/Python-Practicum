from itertools import product


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(sorted(set(input().split(", "))))
    for i in product(*s):
        print("".join(i))


if __name__ == "__main__":
    main()