#  Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти четные числа от 100 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()



from functools import reduce

print("Четные числа от 100 до 1000: ", [el for el in range(100, 1001, 2)])
print("Произведение четных чисел: ", reduce(lambda x, y: x * y, [el for el in range(100, 1001, 2)]))
