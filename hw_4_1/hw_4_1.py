# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

def salary():
    try:
        a = int(input("Production in hours: "))
        b = int(input("Rate per hour: "))
        c = int(input("Premium: "))
        result = a * b + c
        print("The employee's salary was", result, "$")
    except ValueError:
        return print("Error, not a number")

salary()