def main():
    with open("numbers.num", "rb") as f:
        t = f.read()
    print(sum([int.from_bytes(t[i:i + 2], "big") for i in range(0, len(t), 2)]) % 2**16)


if __name__ == "__main__":
    main()