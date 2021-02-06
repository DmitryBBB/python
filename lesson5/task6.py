# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр)

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


with open('task6.txt', 'r', encoding='utf8') as file:
    study = file.readlines()
    lessons = {}
    for line in study:
        inf = line.replace('(', ' ').split()
        lessons[inf[0][:-1]] = sum(int(i) for i in inf if i.isdigit())
    print(f'Общее количество часов по предмету: \n{lessons}')



























#def func(string):
#    try:
 #       numbers = ""
 #       for i in string:
 #           if i.isdigit() is True:
 #               numbers += i
 #       numbers = int(numbers)
 #       return numbers
#    except ValueError:
 #       return 0


#with open('task6.txt', encoding='utf8') as f:
 #  y = f.read().split("\n")[-1]
 #  print(y)
 #  dict = dict()
 #  for item in y:
 #      key = item.split(" ")[0]
 #      value = item.split(" ")[1:]
 #      dict[key] = value

#print(dict)




# for line in f:
     #   subject, lecture, practice, lab = line.split()
      #  obj[subject] = func(lecture) + func(practice) + func(lab)














#my_dict = dict()
#for item in study_list:
    #key = item.split(" ")[0]
    #value = item.split(" ")[1:]
    #my_dict[key] = value
#print(my_dict)








