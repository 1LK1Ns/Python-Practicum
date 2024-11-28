from itertools import product


def main():
    f = input()
    f = f.replace("^", "!=")
    f = f.replace("->", "<=")
    f = f.replace("~", "==")
    f = f.replace("(", "( ")
    f = f.replace(")", " )")
    p = sorted({i for i in f if i.isupper()})
    corr = f.split()
    while "not" in corr:
        br = 0
        corr.insert(corr.index("not"), "(")
        for i in range(corr.index("not") + 1, len(corr) + 1):
            if corr[i] == "(":
                br += 1
            elif corr[i] == ")" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i + 1, ")")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i + 1, ")")
                break
        corr[corr.index("not")] = "."
    while "." in corr:
        corr[corr.index(".")] = "not"
    while "and" in corr:
        br = 0
        for i in range(corr.index("and") - 1, -1, -1):
            if corr[i] == ")":
                br += 1
            elif corr[i] == "(" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i, "(")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i, "(")
                break
        for i in range(corr.index("and") + 1, len(corr) + 1):
            if corr[i] == "(":
                br += 1
            elif corr[i] == ")" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i + 1, ")")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i + 1, ")")
                break
        corr[corr.index("and")] = "."
    while "." in corr:
        corr[corr.index(".")] = "and"
    while "or" in corr:
        br = 0
        for i in range(corr.index("or") - 1, -1, -1):
            if corr[i] == ")":
                br += 1
            elif corr[i] == "(" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i, "(")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i, "(")
                break
        for i in range(corr.index("or") + 1, len(corr) + 1):
            if corr[i] == "(":
                br += 1
            elif corr[i] == ")" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i + 1, ")")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i + 1, ")")
                break
        corr[corr.index("or")] = "."
    while "." in corr:
        corr[corr.index(".")] = "or"
    while "!=" in corr:
        br = 0
        for i in range(corr.index("!=") - 1, -1, -1):
            if corr[i] == ")":
                br += 1
            elif corr[i] == "(" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i, "(")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i, "(")
                break
        for i in range(corr.index("!=") + 1, len(corr) + 1):
            if corr[i] == "(":
                br += 1
            elif corr[i] == ")" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i + 1, ")")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i + 1, ")")
                break
        corr[corr.index("!=")] = "."
    while "." in corr:
        corr[corr.index(".")] = "!="
    while "<=" in corr:
        br = 0
        for i in range(corr.index("<=") - 1, -1, -1):
            if corr[i] == ")":
                br += 1
            elif corr[i] == "(" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i, "(")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i, "(")
                break
        for i in range(corr.index("<=") + 1, len(corr) + 1):
            if corr[i] == "(":
                br += 1
            elif corr[i] == ")" and br != 0:
                br -= 1
                if br == 0:
                    corr.insert(i + 1, ")")
                    break
            elif corr[i].isupper() and br == 0:
                corr.insert(i + 1, ")")
                break
        corr[corr.index("<=")] = "."
    while "." in corr:
        corr[corr.index(".")] = "<="
    f = " ".join(corr)
    al = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print(" ".join([i for i in al[:len(p)]]), "F")
    for i in product(range(2), repeat=len(p)):
        print(" ".join([str(j) for j in i]), int(eval(f, {let: z for let, z in zip(p, i)})))


if __name__ == "__main__":
    main()