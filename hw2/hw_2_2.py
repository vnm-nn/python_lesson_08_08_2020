# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном
# количестве элементов последний сохранить на своем месте. Для заполнения
# списка элементов необходимо использовать функцию input().


while True:
    user_num = input("Enter number: ")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print("Error, not a number!")
list = []
i = 0
element = 0
while i < user_num:
    list.append(input("Enter the following: "))
    i += 1

for elem in range(int(len(list)/2)):
        list[element], list[element + 1] = list [element + 1], list[element]
        element += 2
print(list)