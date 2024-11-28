from itertools import permutations


def main():
    p = (" ".join([" ".join(input().split(", ")) for _ in range(int(input()))])).split()
    for i in permutations(sorted(p), 3):
        print(" ".join(i))


if __name__ == "__main__":
    main()