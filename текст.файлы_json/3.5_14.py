import json


def main():
    with open((u := input()), encoding="UTF-8") as f:
        d1 = json.load(f)
    with open(input(), encoding="UTF-8") as f:
        d2 = json.load(f)
    d = {i["name"]: {k: v for k, v in i.items() if k != "name"} for i in d1}
    for i in d2:
        if i["name"] in d:
            for j in i:
                if (j not in d[i["name"]] or i[j] > d[i["name"]][j]) and j != "name":
                    d[i["name"]][j] = i[j]
        else:
            d[i["name"]] = {k: v for k, v in i.items() if k != "name"}
    with open(u, "w", encoding="UTF-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()