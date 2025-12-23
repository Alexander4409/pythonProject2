#Операторы
# +, -, *, ** - Степень, /, // - Целочисленное деление, % - остаток
# Операторы с присваиванием
# += - инкримент
# -= - декримент
# *=, /= , //=, %=
# = - присваивания
# num = 1000
# num += 10
# print(num)
# num *= 10
# print(num)
#
# first_num = 21212.523534534534
# second_num = 42
# res = first_num / second_num
# print(round(res,5))

#Операторы сравнения
# == - Проверяет равенство
# >, <, <= , >= - больше меньше либо равно
#!= - не равенство
# res = 3 != 6
# print(res)
# num_1 = 2
# num_2 = 4
# res = num_1 + num_2
# num_1, num_2 - операнды

#Логические операторы
# and, or, not, in,
# and - логическое умножение
# age = 17
# passport = True
# res = age > 18 and passport
# print(res)
#
# age == 20
# weight <= 100

# age = 19
# is_married = True
# res = age > 18 or is_married
# print(res)

#in
# message = "hello world"
# world = "world"
# print(world in message)
#
# black = "black"
# print(black in message)


# Условные операторы
# if, elif, else
language = ""

if language == "English":
    print("Hello")
elif language == "Russian":
    print("Привет")
elif language == "German":
    print("Welt")
else:
    print("language is not detected")

print("End")
# погодные условия