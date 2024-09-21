def main():
    p = int(input())
    v = int(input())
    t = int(input())
    if max(p, v, t) == p:
        print('1. Петя')
    elif max(p, v, t) == v:
        print('1. Вася')
    else:
        print('1. Толя')
    if max(p, v, t) != p and min(p, v, t) != p:
        print('2. Петя')
    elif max(p, v, t) != v and min(p, v, t) != v:
        print('2. Вася')
    else:
        print('2. Толя')
    if min(p, v, t) == p:
        print('3. Петя')
    elif min(p, v, t) == v:
        print('3. Вася')
    else:
        print('3. Толя')
if __name__ == '__main__':
    main()
