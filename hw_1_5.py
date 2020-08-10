# 5. Запросите у пользователя значения выручки
# и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка
# больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью,
# вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете
# на одного сотрудника.

earnings = int(input("Enter earnings: "))
cost = int(input("Enter cost: "))

if earnings > cost:
    profit = ((earnings - cost) / earnings) * 100
    print(f"Good work, you have: {profit:.1f} % profitability")
    workers = int(input("Enter the number of the employees: "))
    print(f"Earnings for one worker: {(earnings - cost) / workers:.1f}")
elif earnings == cost:
    print("Not bad.")
else:
    print("You have a loss.")
