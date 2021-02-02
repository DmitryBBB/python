
#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division (*args):
    while True:
        try:
            num1 = int(input("Введите число: "))
            num2 = int(input("Введите число: "))
            number = (num1 / num2)
            return number
        except Exception as s:
            print("делить на 0 нельзя")

print(division())



