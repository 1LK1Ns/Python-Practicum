def main():
    n = int(input())
    for i in range(n):
        s = input()
        if s.find('зайка') == -1:
            print('Заек нет =(')
        else:
            print(s.find('зайка') + 1)


if __name__ == '__main__':
    main()