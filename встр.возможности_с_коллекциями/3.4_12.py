def main():
    p = (" ".join([" ".join(input().split(", ")) for _ in range(int(input()))])).split()
    for i, j in enumerate(sorted(p), 1):
        print(f"{i}. {j}")


if __name__ == "__main__":
    main()