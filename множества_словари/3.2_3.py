def main():
    a = " ".join([input() for _ in range(int(input()))]).split()
    for i in set(a):
        print(i)


if __name__ == "__main__":
    main()