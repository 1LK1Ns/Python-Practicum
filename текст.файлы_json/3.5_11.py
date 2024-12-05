import json


def main():
    with open(input(), encoding="UTF-8") as f:
        t = " ".join(f.read().split("\n")).split()
    t = [int(i) for i in t]
    ans = {"count": len(t), "positive_count": len([i for i in t if i > 0]), "min": min(t), "max": max(t),
           "sum": sum(t), "average": float(f"{sum(t) / len(t):.2f}")}
    with open(input(), "w", encoding="UTF-8") as f:
        json.dump(ans, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()