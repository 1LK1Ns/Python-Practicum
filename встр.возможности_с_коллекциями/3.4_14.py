from itertools import permutations


def main():
    for i in permutations(sorted([input() for _ in range(int(input()))]), r=3):
        print(", ".join(i))


if __name__ == "__main__":
    main()