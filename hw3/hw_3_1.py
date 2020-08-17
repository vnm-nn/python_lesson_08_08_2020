# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_f ():
    '''
    while True:
        num_1 = input("Enter 1st number: ")
        if num_1.isdigit():
            num_1 = int(num_1)
            break
        print("Error, not a number!")
    while True:
        num_2 = input("Enter 2nd number: ")
        if num_2.isdigit():
            num_2 = int(num_2)
            break
        print("Error, not a number!")
    if num_2 != 0:
        div = num_1 / num_2
    else:
        print("Error, zero")
    print("Result division: ", div)
    '''
    try:
        num_1 = int(input("Enter 1st number: "))
        num_2 = int(input("Enter 2nd number: "))
        res = num_1 / num_2
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Error, you cannot divide by zero"
    #print("Result: ", res)
    return res

# my_f()
print(f"res {my_f()}")