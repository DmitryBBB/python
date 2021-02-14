class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()


____________________________________________________


# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self, direction):
        self.direction = direction
        return f"Машина повернула на {direction}"
    def show_speed(self):
        return f"Машина движется со скоростью: {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} двигается со скоростью {self.speed} вы привысили лимит скорости 60"
        else:
            return f"{self.name} скорость {self.speed} Вы двигаетесь с разрешенной скоростью"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} двигается со скоростью {self.speed} вы привысили лимит скорости 40"
        else:
            return f"{self.name} скорость {self.speed} Вы двигаетесь с разрешенной скоростью"

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town = TownCar(70, "Синий", "Ford",False)
print(f'Машина: {town.name}\n Цвет: {town.color}\n {town.go()}\n {town.show_speed()}\n {town.turn("налево")}\n {town.stop()}')
print("----------------------------------")

work = WorkCar(50, "Красный", "Chevrolet",False)
print(f'Машина: {work.name}\n Цвет: {work.color}\n {work.go()}\n {work.show_speed()}\n {work.turn("налево")}\n {work.stop()}')
print("----------------------------------")

sport = SportCar(280, "Красный", "Ferrari",False)
print(f'Машина: {sport.name}\n Цвет: {sport.color}\n {sport.go()}\n {sport.show_speed()}\n {sport.turn("налево")}\n {sport.stop()}')
print("----------------------------------")

police = PoliceCar(120, "Бело-Синий", "Приора",True)
print(f'Машина: {police.name}\n Цвет: {police.color}\n {police.go()}\n {police.show_speed()}\n {police.turn("налево")}\n {police.stop()}')


__________________________________________________
      
      
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Василий', 'Яковлев', 'Инженер', '100000', '50000')
print(p.get_full_name(), p.get_total_income())

_______________________________________________________________
      
      
      
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.      

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} красит')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()      
      
      
