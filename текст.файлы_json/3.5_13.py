from sys import stdin
import json


def main():
    t = stdin.read().split("\n")
    with open(t[0], encoding="UTF-8") as f:
        d = json.load(f)
    for i in t[1:]:
        k = i.split(" == ")
        d[k[0]] = k[1]
    with open(t[0], "w", encoding="UTF-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()