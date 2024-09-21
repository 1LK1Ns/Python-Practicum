def main():
    p = input()
    c = int(input())
    w = int(input())
    m = int(input())
    print("Чек")
    print(f"{p} - {w}кг - {c}руб/кг")
    print(f"Итого: {c * w}руб")
    print(f"Внесено: {m}руб")
    print(f"Сдача: {m - c * w}руб")
if __name__ == '__main__':
    main()
