def month(n, m="ru"):
    en = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
    ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    return en[n - 1] if m == "en" else ru[n - 1]