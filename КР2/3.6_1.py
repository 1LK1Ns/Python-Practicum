def main():
    for _ in range(int(input())):
        s = input().split("&")
        print(s[2][int(s[0])::2][:int(s[1])])


if __name__ == "__main__":
    main()