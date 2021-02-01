words = input("Введите набор слов через пробел: ").split()
i = 1
for say in words:
    print(f'№{i} {say[0:10]}\n')
    i += 1
print()