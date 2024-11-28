from itertools import product


def main():
    n = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
    m = ["пик", "треф", "бубен", "червей"]
    m.remove(input())
    for i, j in product(n, m):
        print(i, j)


if __name__ == "__main__":
    main()