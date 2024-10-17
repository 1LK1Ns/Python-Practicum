def main():
    opn = input().split()
    while len(opn) > 1:
        for i in range(len(opn)):
            if not opn[i].isdigit():
                if opn[i] == '*':
                    a = int(opn[i - 2]) * int(opn[i - 1])
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.insert(i - 2, str(a))
                    break
                if opn[i] == '+':
                    a = int(opn[i - 2]) + int(opn[i - 1])
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.insert(i - 2, str(a))
                    break
                if opn[i] == '-':
                    a = int(opn[i - 2]) - int(opn[i - 1])
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.insert(i - 2, str(a))
                    break
                if opn[i] == '!':
                    a = int(opn[i - 1])
                    for j in range(2, int(opn[i - 1])):
                        a *= j
                    opn.pop(i - 1)
                    opn.pop(i - 1)
                    opn.insert(i - 1, str(a))
                    break
                if opn[i] == '/':
                    a = int(opn[i - 2]) // int(opn[i - 1])
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.pop(i - 2)
                    opn.insert(i - 2, str(a))
                    break
                if opn[i] == '~':
                    a = -int(opn[i - 1])
                    opn.pop(i - 1)
                    opn.pop(i - 1)
                    opn.insert(i - 1, str(a))
                    break
                if opn[i] == '#':
                    a = int(opn[i - 1])
                    opn.pop(i)
                    opn.insert(i, str(a))
                    break
                if opn[i] == '@':
                    a = int(opn[i - 3])
                    b = int(opn[i - 2])
                    c = int(opn[i - 1])
                    opn.pop(i - 3)
                    opn.pop(i - 3)
                    opn.pop(i - 3)
                    opn.pop(i - 3)
                    opn.insert(i - 3, str(a))
                    opn.insert(i - 3, str(c))
                    opn.insert(i - 3, str(b))
                    break
    print(opn[0])


if __name__ == '__main__':
    main()