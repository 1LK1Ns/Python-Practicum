def main():
    with open(input(), encoding="UTF-8") as f:
        t = f.read().split("\n")
    for i in t[len(t) - int(input()) - 1:-1]:
        print(i)


if __name__ == "__main__":
    main()