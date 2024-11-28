from itertools import combinations


def main():
    p = [input() for _ in range(int(input()))]
    for i, j in combinations(p, 2):
        print(f"{i} - {j}")


if __name__ == "__main__":
    main()