def main():
    a = dict()
    for _ in range(int(input())):
        s = input()
        a[s] = a.get(s, 0) + 1
    for i in sorted(a):
        if sum([a[i] for i in a if a[i] != 1]) != 0:
            print(f"{i} - {a[i]}\n" if a[i] != 1 else "", end="")
        else:
            print("Однофамильцев нет")
            break


if __name__ == "__main__":
    main()