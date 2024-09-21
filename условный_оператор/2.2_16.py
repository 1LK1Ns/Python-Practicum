def main():
    p = int(input())
    v = int(input())
    t = int(input())
    pp = 'Петя'
    vv = 'Вася'
    tt = 'Толя'
    n1 = 'I'
    n2 = 'II'
    n3 = 'III'
    if max(p, v, t) == p:
        print(f'{pp:^24}')
    elif max(p, v, t) == v:
        print(f'{vv:^24}')
    else:
        print(f'{tt:^24}')
    if max(p, v, t) != p and min(p, v, t) != p:
        print(f'  {pp:<6}')
    elif max(p, v, t) != v and min(p, v, t) != v:
        print(f'  {vv:<6}')
    else:
        print(f'  {tt:<6}')
    if min(p, v, t) == p:
        print(f'{pp:>22}  ')
    elif min(p, v, t) == v:
        print(f'{vv:>22}  ')
    else:
        print(f'{tt:>22}  ')
    print(f'{n2:^8}{n1:^8}{n3:^8}')
if __name__ == '__main__':
    main()
