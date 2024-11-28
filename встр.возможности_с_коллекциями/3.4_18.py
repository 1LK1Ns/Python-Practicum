from itertools import product


def main():
    print("a b c f")
    f = input()
    for a, b, c in product(range(2), repeat=3):
        print(a, b, c, int(eval(f)))


if __name__ == "__main__":
    main()