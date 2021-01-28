#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func (arg1, arg2, arg3):
    z = [arg1, arg2, arg3]
    z.remove(min(z))
    return sum(z)


print(my_func(3,2,4))