def main():
    s = input()
    n = int(input())
    print(f"Группа №{n // 100}.")
    print(f"{n % 10}. {s}.")
    print(f"Шкафчик: {n}.")
    print(f"Кроватка: {n // 10 % 10}.")
if __name__ == '__main__':
    main()
