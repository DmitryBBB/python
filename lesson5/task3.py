# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
# окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


salary_list = []
with open("text3.txt", "r", encoding="utf-8") as func:


    for surname in func.readlines():
        salary_list.append(int(surname.split()[1]))
        if int(surname.split()[1]) < 20000:
            print("Оклад меньше 20тыс. : ", surname.split()[0])
    print("Средняя зарплата на предприятии: ", sum(salary_list)/len(salary_list))


