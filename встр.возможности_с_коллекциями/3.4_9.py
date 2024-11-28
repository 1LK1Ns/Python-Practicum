from itertools import product


def main():
    n = int(input())
    for i, j in product(range(1, n + 1), range(1, n + 1)):
        print(i * j, end=" ")
        if j == n:
            print()


if __name__ == "__main__":
    main()