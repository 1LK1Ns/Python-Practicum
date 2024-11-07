def main():
    c = set()
    a = set(input() for _ in range(int(input())))
    for _ in range(int(input())):
        k = input()
        b = set(input() for _ in range(int(input())))
        if b <= a:
            c.add(k)
    print("\n".join([i for i in sorted(c)]) if len(c) != 0 else "Готовить нечего")


if __name__ == "__main__":
    main()