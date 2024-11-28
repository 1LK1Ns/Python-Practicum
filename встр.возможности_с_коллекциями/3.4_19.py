from itertools import product


def main():
    f = input()
    p = sorted({i for i in f if i.isupper()})
    al = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print(" ".join([i for i in al[:len(p)]]), "F")
    for i in product(range(2), repeat=len(p)):
        print(" ".join([str(j) for j in i]), int(eval(f, {let: z for let, z in zip(p, i)})))


if __name__ == "__main__":
    main()