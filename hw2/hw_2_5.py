# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например,
# my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Rating - {my_list}")

while True:
    user_num = input("Enter number (0 - Exit): ")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print("Error, not a number!")

while user_num != 0:
    for el in range(len(my_list)):
        if my_list[el] == user_num:
            my_list.insert(el + 1, user_num)
            break
        elif my_list[0] < user_num:
            my_list.insert(0, user_num)
        elif my_list[-1] > user_num:
            my_list.append(user_num)
        elif my_list[el] > user_num and my_list[el + 1] < user_num:
            my_list.insert(el + 1, user_num)
    print(f"Rating - {my_list}")
    user_num = int(input("Enter number (0 - Exit): "))