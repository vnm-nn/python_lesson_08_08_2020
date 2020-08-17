# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов

def my_f(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3

print(f'Result: {my_f(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")), int(input("Enter 3rd number: ")))}')