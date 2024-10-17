def main():
    s = input()
    while s != '':
        c = 1
        for i in range(len(s)):
            if i != len(s) - 1 and s[i] == s[i + 1]:
                c += 1
            else:
                print(s[i], c)
                s = s[i + 1:]
                break


if __name__ == '__main__':
    main()