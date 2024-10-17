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
    print(opn[0])


if __name__ == '__main__':
    main()