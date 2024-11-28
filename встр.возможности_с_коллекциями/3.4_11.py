from itertools import product


def main():
    n = int(input())
    m = int(input())
    ml = len(str(n * m))
    for i, j in product(range(1, n * m + 1), repeat=2):
        if j % m != 0:
            print(f"{j:>{ml}}", end=" ")
        elif j % (n * m) == 0:
            print(f"{j:>{ml}}")
            break
        else:
            print(f"{j:>{ml}}")


if __name__ == "__main__":
    main()