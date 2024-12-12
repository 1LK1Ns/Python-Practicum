def order(*c):
    global in_stock
    rec = {"Эспрессо": (1, 0, 0), "Капучино": (1, 3, 0), "Макиато": (2, 1, 0),
           "Кофе по-венски": (1, 0, 2), "Латте Макиато": (1, 2, 1), "Кон Панна": (1, 0, 1)}
    for i in c:
        if rec[i][0] <= in_stock["coffee"] and rec[i][1] <= in_stock["milk"] \
           and rec[i][2] <= in_stock["cream"]:
            in_stock["coffee"] -= rec[i][0]
            in_stock["milk"] -= rec[i][1]
            in_stock["cream"] -= rec[i][2]
            return i
    return "К сожалению, не можем предложить Вам напиток"