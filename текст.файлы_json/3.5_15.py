import json


def main():
    s = 0
    with open("scoring.json", encoding="UTF-8") as f:
        t = json.load(f)
    for i in t:
        for j in i["tests"]:
            if j["pattern"] == input():
                s += int(i["points"]) / len(i["tests"])
    print(int(s))


if __name__ == "__main__":
    main()