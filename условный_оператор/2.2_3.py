def main():
    p = int(input())
    v = int(input())
    t = int(input())
    if max(p, v, t) == p:
        print("Петя")
    elif max(p, v, t) == v:
        print("Вася")
    else:
        print("Толя")
if __name__ == '__main__':
    main()
