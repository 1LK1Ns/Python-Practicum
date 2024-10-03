def main():
    n = input()
    s = ''
    for i in n:
        if int(i) % 2 == 1:
            s += i
    print(s)


if __name__ == '__main__':
    main()