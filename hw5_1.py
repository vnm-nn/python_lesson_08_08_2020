# 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

my_f = open('text.txt', 'w', encoding='UTF-8')
line = input('Enter text: \n')
while line:
    my_f.writelines(line)
    line = input('Enter text: \n')
    if not line:
        break

my_f.close()
my_f = open('text.txt', 'r', encoding='UTF-8')
content = my_f.readlines()
print(content)
my_f.close()