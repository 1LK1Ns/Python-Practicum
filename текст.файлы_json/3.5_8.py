def main():
    with open(input(), encoding="UTF-8") as f:
        t1 = " ".join(f.read().split("\n")).split()
    with open(input(), encoding="UTF-8") as f:
        t2 = " ".join(f.read().split("\n")).split()
    with open(input(), "w", encoding="UTF-8") as f:
        f.write("\n".join(sorted(set(t1) ^ set(t2))))


if __name__ == "__main__":
    main()