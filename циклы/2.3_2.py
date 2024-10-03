def main():
    c = 0
    while (s := input()) != 'Приехали!':
        if 'зайка' in s:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
