def main():
    nb = 1001
    nm = 1
    print((nb + nm) // 2)
    while (s := input()) != 'Угадал!':
        if s == 'Меньше':
            nb = (nb + nm) // 2
        if s == 'Больше':
            nm = (nb + nm) // 2
        print((nb + nm) // 2)


if __name__ == '__main__':
    main()