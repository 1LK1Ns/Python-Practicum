from sys import stdin


def main():
    ans = []
    text = set(" ".join(stdin.read().split("\n")).split())
    for i in text:
        if i.lower() == i.lower()[::-1]:
            ans.append(i)
    for i in sorted(ans):
        print(i)


if __name__ == "__main__":
    main()