# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

#def my_f ():
#    info_d = {"name": "", "surname": "", "year": "", "city": "", "email": "", "phone": ""}
#    for key, value in info_d.items():
#        print(", ".join(info_d.values()))

def my_f ():
    info_dict = {}
    info_dict["name"] = str(input("Enter name: "))
    info_dict["surname"] = str(input("Enter surname: "))
    info_dict["birth_year"] = str(input("Enter year of birth: "))
    info_dict["city"] = str(input("Enter your city: "))
    info_dict["email"] = str(input("Enter email: "))
    info_dict["phone"] = str(input("Enter phone: "))
    print (', '.join(info_dict.values()))
my_f()
