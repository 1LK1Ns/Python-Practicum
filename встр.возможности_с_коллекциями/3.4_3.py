from itertools import count


def main():
    s, e, c = map(float, input().split())
    for i in count(s, c):
        if i < e:
            print(f"{i:.2f}")
        else:
            break


if __name__ == "__main__":
    main()