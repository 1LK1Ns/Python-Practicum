def main():
    p = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
    n = int(input())
    for i in range(n):
        print(p[i % 5])


if __name__ == '__main__':
    main()