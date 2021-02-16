# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, x):
        self.x = x


def division():
    try:
        numb_1 = int(input("Введите число: "))
        numb_2 = int(input("Введите делитель: "))
        if numb_2 == 0:
            raise ZeroError("Делить на 0 нельзя")
        else:
            result = numb_1 / numb_2
            return result
    except ValueError:
        return "Вы ввели не число"
    except ZeroError as y:
        return y

print(division())
