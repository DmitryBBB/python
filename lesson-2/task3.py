

season = {
    1: ["Зима"],
    2: ["Зима"],
    3: ["Весна"],
    4: ["Весна"],
    5: ["Весна"],
    6: ["Лето"],
    7: ["Лето"],
    8: ["Лето"],
    9: ["Осень"],
    10: ["Осень"],
    11: ["Осень"],
    12: ["Зима"]

}
while True:
    month = input("Введите номер месяца: ")
    if not month.isdigit() or int(month) > 12 or int(month) < 1:
        print("Введите корректное значение от 1 до 12")
    else:
        month = int(month)
        break
print(month, " месяц это - ", season[month][0])

