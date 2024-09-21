def main():
    print("Как Вас зовут?")
    n = input()
    print(f"Здравствуйте, {n}!")
    print("Как дела?")
    s = input()
    if s == 'хорошо':
        print("Я за вас рада!")
    elif s == 'плохо':
        print("Всё наладится!")
if __name__ == '__main__':
    main()
