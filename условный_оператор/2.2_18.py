def main():
    a = int(input())
    b = int(input())
    c = int(input())
    m = max(a, b, c)
    mi = min(a, b, c)
    if m ** 2 == mi ** 2 + (a + b + c - m - mi) ** 2:
        print('100%')
    elif m ** 2 > mi ** 2 + (a + b + c - m - mi) ** 2 and m < a + b + c - m:
        print('велика')
    elif m ** 2 < mi ** 2 + (a + b + c - m - mi) ** 2 and m < a + b + c - m:
        print('крайне мала')
if __name__ == '__main__':
    main()
