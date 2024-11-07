def main():
    n = int(input())
    m = int(input())
    a = set([input() for _ in range(n)])
    b = set([input() for _ in range(m)])
    print("Таких нет" if len(a & b) == 0 else len(a & b))


if __name__ == "__main__":
    main()