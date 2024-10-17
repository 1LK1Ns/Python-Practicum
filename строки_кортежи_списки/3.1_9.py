def main():
    s = input()
    while s != '':
        i = s.find('#')
        if i == 0:
            pass
        elif i == -1:
            print(s)
        else:
            print(s[:i])
        s = input()


if __name__ == '__main__':
    main()