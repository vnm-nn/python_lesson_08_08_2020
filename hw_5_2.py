# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('hw_2.txt', 'r')
content = my_file.read()

print(f'Content: \n {content}')

my_file = open('hw_2.txt', 'r')
content = my_file.readlines()
print(f'Number of lines in the file - {len(content)}')
my_file = open('hw_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Number of characters in a line {i + 1} {len(content[i])}')
my_file = open('hw_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Word count - {len(content)}')
my_file.close()