# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_list = ("winter", "spring", "summer", "autumn")
my_tuple = {1 : "winter", 2 : "spring", 3 : "summer", 4 : "autumn"}
min = 1
max = 12

while True:
    user_num = input("Enter number 1 - 12: ")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print("Error, not a number or wrong number!")

if user_num == 1 or user_num == 2 or user_num == 12:
    print("Season is", my_tuple.get(1))
elif user_num == 3 or user_num == 4 or user_num == 5:
    print("Season is", my_tuple.get(2))
elif user_num == 6 or user_num == 7 or user_num == 8:
    print("Season is", my_tuple.get(3))
elif user_num == 9 or user_num == 10 or user_num == 11:
    print("Season is", my_tuple.get(4))
else:
    print("Something wrong")