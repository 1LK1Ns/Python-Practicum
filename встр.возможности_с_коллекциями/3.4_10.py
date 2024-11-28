from itertools import product


def main():
    print("А Б В")
    for i, j in product(range(1, (n := int(input())) - 1), repeat=2):
        if i + j < n:
            print(i, j, n - i - j)


if __name__ == "__main__":
    main()