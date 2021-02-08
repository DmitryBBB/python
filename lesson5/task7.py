# Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
#profit = dict()
#profit_summ = {}
#profit_firm = []
#with open("task7.txt", "r") as company:
    #firm = company.read().split("\n")
    #for item in firm:
        #key = item.split(" ")[0]
        #value = item.split(" ")[2:]
        #profit[key] = value
    #profit.popitem()
    #print(profit)
profit = {}
profit_firms = []
with open("task7.txt", "r", encoding="utf-8") as firms:

    while True:
        line = firms.readline().split()
        if not line:
            break
        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            profit_firms.append(profit[line[0]])
        else:
            unprofitable_firm = (profit[line[0]])
            del profit[line[0]]

    print(profit_firms)
    print(unprofitable_firm)
result = [profit, {"average_profit": sum(profit_firms) / len(profit_firms)}, {"unprofitable_firm": unprofitable_firm}]
print(result)

import json
with open("file.json", 'w', encoding='utf-8') as file_j:
    json.dump(result, file_j)
















