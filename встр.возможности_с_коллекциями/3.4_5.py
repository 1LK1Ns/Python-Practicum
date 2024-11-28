def main():
    s = sorted(input().split(", ") + input().split(", ") + input().split(", "))
    for i, j in enumerate(s, 1):
        print(f"{i}. {j}")


if __name__ == "__main__":
    main()