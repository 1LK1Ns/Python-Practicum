def main():
    s = input()
    while s != '':
        if s.endswith('@@@'):
            pass
        elif s.startswith('##'):
            print(s[2:])
        else:
            print(s)
        s = input()


if __name__ == '__main__':
    main()