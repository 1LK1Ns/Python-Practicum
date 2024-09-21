def main():
    p = input()
    c = int(input())
    w = int(input())
    m = int(input())
    h = "Чек"
    L2 = f"{w}кг * {c}руб/кг"
    print(f"{h:=^35}")
    print(f"Товар:{p:>29}")
    print(f"Цена:{L2:>30}")
    print(f"Итого:{w * c:>26}руб")
    print(f"Внесено:{m:>24}руб")
    print(f"Сдача:{m - w * c:>26}руб")
    print("=" * 35)
if __name__ == '__main__':
    main()
