#  Создать программно файл в текстовом формате, записать в него построчно данные,
#  вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

my_file = open("text1.txt", "w")
words = input("Введите текст: \n")

while words:
    my_file.writelines(words)
    words = input("Введите текст: \n")
    if not words:
        break


my_file.close()

my_file = open("text1.txt", "r")
read = my_file.readlines()
print(read)
my_file.close()