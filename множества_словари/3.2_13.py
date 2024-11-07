def main():
    c = set()
    a = set(input() for _ in range(int(input())))
    for _ in range(int(input())):
        b = set(input() for _ in range(int(input())))
        c = b | c
    print("\n".join([i for i in sorted(a ^ c)]) if len(a ^ c) != 0 else "Готовить нечего")


if __name__ == "__main__":
    main()