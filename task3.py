# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NumbOnlyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'Добавляем "{user_val}" в список. Нажмите Еnter для завершения: ')
                    self.my_list.append(user_val)
                    if ex == '':
                        print(self.my_list)
                        break
                except ValueError:
                    raise NumbOnlyError
            except NumbOnlyError:
                ex = input(f"Вы ввели не число! Нажмите Еnter для завершения: ")
                if ex == '':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()

