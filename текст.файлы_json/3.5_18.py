import os


def main():
    s = os.path.getsize(input())
    if s >= 1024 ** 3:
        s = int(s / 1024 ** 3) + 1
        t = "ГБ"
    elif s >= 1024 ** 2:
        s = int(s / 1024 ** 2) + 1
        t = "МБ"
    elif s >= 1024:
        s = int(s / 1024) + 1
        t = "КБ"
    else:
        t = "Б"
    print(f"{s}{t}")


if __name__ == "__main__":
    main()