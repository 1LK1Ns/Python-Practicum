def main():
    x = 0
    y = 0
    while (s := input()) != 'СТОП':
        n = int(input())
        if s == 'СЕВЕР':
            x += n
        if s == 'ЮГ':
            x -= n
        if s == 'ВОСТОК':
            y += n
        if s == 'ЗАПАД':
            y -= n
    print(x)
    print(y)


if __name__ == '__main__':
    main()