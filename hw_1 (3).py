# Узнайте у пользователя число n. Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = int(input("Enter number: "))
a = int(str(num) + str(num))
print(a)
b = int(str(num) + str(num) + str(num))
summ = num + a + b
print(summ)
