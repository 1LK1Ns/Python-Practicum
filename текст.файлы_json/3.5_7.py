def main():
    with open(input(), encoding="UTF-8") as f:
        t = " ".join(f.read().split("\n")).split()
    t = [int(i) for i in t]
    print(len(t))
    print(len([i for i in t if i > 0]))
    print(min(t))
    print(max(t))
    print(sum(t))
    print(f"{sum(t) / len(t):.2f}")


if __name__ == "__main__":
    main()