def main():
    n = input()
    s = 0
    for i in n:
        if int(i) > s:
            s = int(i)
    print(s)


if __name__ == '__main__':
    main()