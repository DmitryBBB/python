# Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_txt = open("text2.txt", encoding="utf-8")
line = 0

for i, tx in enumerate(my_txt.readlines(), 1):
    line = i
    print("Строка №: ", i, " Количество слов: ", len(tx.split()))
print("Количество строк: ", line)

my_txt.close()


