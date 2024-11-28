from itertools import product


def main():
    n = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
    m = ["бубен", "пик", "треф", "червей"]
    match a := input():
        case "пики":
            a = "пик"
        case "буби":
            a = "бубен"
        case "трефы":
            a = "треф"
        case "черви":
            a = "червей"
    n.remove(input())
    c = 0
    for i in product(n, m, repeat=3):
        k1 = f"{i[0]} {i[1]}"
        k2 = f"{i[2]} {i[3]}"
        k3 = f"{i[4]} {i[5]}"
        if k1 < k2 < k3 and a in i:
            print(f"{k1}, {k2}, {k3}")
            c += 1
        if c == 10:
            break


if __name__ == "__main__":
    main()