

max = int(input("Введите количество элементов списка "))
box = []
i = 0
el = 0
while i < max:
    box.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(box)/2)):
        box[el], box[el + 1] = box [el + 1], box[el]
        el += 2
print(box)