from sys import stdin


def main():
    text = stdin.read().split("\n")[:-1]
    ans = []
    for i in text:
        if text[-1].lower() in i.lower():
            ans.append(i)
    for i in ans[:-1]:
        print(i)


if __name__ == "__main__":
    main()