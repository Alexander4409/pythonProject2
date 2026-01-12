#def - функции, позволяют выполнять определенную процедуру много раз
# def имя_функции ([параметры]):
#     инструкции

#Процедура(инструкция)
# def say_name(name):
#     print(name)
#
#
# say_name("Tom")
# say_name("John")
# say_name("Marry")
# say_name("Nancy")

# return - оператор, который возвращает некое значение

# Настоящая функция т.к есть return
# def say_name(name):
#      return f"Hello {name}"
#
# print(say_name("John Doe"))


# Локальные функции
# def print_messages():
#     #определение локальных функций
#     def say_hi():print("Hi")
#
#     def say_by():print("Bye")
#
#     say_by()
#     say_hi()
#
# print_messages()

#Организация работы программы

# def main():
#     say_bye()
#     say_hi()
#
# def say_hi():
#     print("Hi")
#
# def say_bye():
#     print("Bye")
#
# main()

#Параметры функции
# def say_hello(name):
#     print(f"Hello, {name}")
#
#
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")
#Параметры функции
# def print_user_data(name, age, OS):
#     print(f"Name: {name}\n"
#           f"Age: {age}\n"
#           f"Operation system: {OS}\n")
#
# print_user_data("Tom", 18, "Android")


#ДЗ 1
#Написать 2 функции которые будут выполнять различные математические операции
# на выбор , +, - , /  ,*  ,** важно,
# порядок вызова этих функций определяет пользователь,
# пользователь должен вызвать все функции.
# Использовать условные операторы, и добавить очередность вызова функций с
# использованием функции main


#Дз 2
# Написать функцию, которая принимает модель, марку, тип кузова, объем двигателя, цвет автомобиля
# и выводит информацию в консоль пример:
# Модель: Toyota
# Марка: Corolla
# Тип кузова: Седан
# Объем двигателя: 1.8
# Цвет: Красный

# курс степик для начинающих - https://stepik.org/course/58852/promo
# курс степик для продвинутых - https://stepik.org/course/68343/promo
# срок прохождения до конца мая 2026!


# материал лекции - https://metanit.com/python/tutorial/2.15.php