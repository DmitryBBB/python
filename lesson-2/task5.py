my_list = [8, 6, 6, 4, 2]
user_num = int(input("Введите число"))
for el in range(len(my_list)):
    if my_list[el] == user_num:
        my_list.insert(el + 1, user_num)
        break
    elif my_list[-1] > user_num:
        my_list.append(user_num)
    elif my_list[0] < user_num:
        my_list.insert(0, user_num)
    elif my_list[el] > user_num and my_list[el +1] < user_num:
        my_list.insert(el + 1, user_num)
print(my_list)
