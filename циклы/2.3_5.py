def main():
    s = 0
    while (n := float(input())) != 0:
        if n >= 500:
            s += 0.9 * n
        else:
            s += n
    print(s)


if __name__ == '__main__':
    main()