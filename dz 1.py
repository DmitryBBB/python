print("Задание 1")
a = "Pyton"
print(a)

b = 56
print(b)

c = int(input("Введите число "))
print("Ваше число: ", c)

r = input("Вы любите прграммировать? ")
print(r , ", ваш выбор")

print("Задание 2")

time = int(input("Введите время в секундах "))

hourse = (time // 3600)
minits = (time % 3600) // 60
second = (time % 3600) % 60
print(hourse, minits, second, sep=":")

print("Задание №3")

n = int(input("Введите число "))
num1 = str(n) + str(n)
num2 = str(n) + str(n) +str(n)
summ = n + int(num1) + int(num2)
print(summ)

print("Задание №4")

a = int(input())
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

print("Задание 5")

revenue = int(input("Введите выручку: "))
costs = int(input("Введите затраты: "))
peopls = int(input("Введите количество сотрудников"))
margin = revenue - costs
print("Прибыль составит: ", margin)
if revenue > costs:
    print("Вы в плюсе")
    pay = margin / peopls
    print("Какждый сотрудник получит по ", pay)
    rent = (revenue / costs) * 100
    print("Рентабельность составит ", rent, "%")
else:
    print("Вы в минусе")


print("Задание 6")

a = int(input("Введите расстояние в км которое вы приодолели в первый день "))
b = int(input("Введите расстояние которого хотите достигнуть, увеличивая результат на 10% каждый день от начального "))
days = 1
print("На ", days, "день ", a, " км")
while b >= a:

    days += 1
    a = a + (a * 0.1)

print("На ", days, "день ", a, " км")






