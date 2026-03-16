#Второй урок Словари
#Перебор словарей items()
from new.new_web_lesson_12 import users_dict

# users_dict = {
#     '12345': 'Tom',
#     '54321': 'Mary',
#     '15243': 'Bob'
# }
#
# for phone_number, user_name in users_dict.items():
#     print(f'Phone:{phone_number} User_name: {user_name}')

# users = {
#     "Tom" : {"Phone" : 9999,
#              "email": "user@maii.ru"},
#
#     "Bob" : {"Phone" : 8888,
#              "email": "user_1@gmail.com",
#              "tel.me":12313123}
# }
#
# get_email = users["Tom"]["email"]
# print(get_email)
#
# bob_telegramm = users["Bob"].get("tel78.me","No Data")
# print(bob_telegramm)

# products_catalog = {
#     "Яблоки": {
#         "calories_per_100g": 52,
#         "items_in_package": 6
#     },
#     "Йогурт": {
#         "calories_per_100g": 85,
#         "items_in_package": 4
#     },
#     "Протеиновые батончики": {
#         "calories_per_100g": 410,
#         "items_in_package": 12
#     },
#     "Куринные яйца": {
#         "calories_per_100g": 155,
#         "items_in_package": 10
#     }
# }


################################### Множества set() ###################################
# users = {"Anna", "Bob", "Sam", "Anna"}
# print(users)

# user_list = ["Anna", "Bob", "Sam", "Anna"]
#
# users_set = set(user_list)
# print(user_list)
# print(len(users_set))

# удаление элементов из множества
# remove - генерирует исключения при отсутствии элемента в множестве
# discard - дружелюбный не генерит исключений
# clear - удаляет все элементы в множестве
# user = "Bob"
#
# print(users)

# перебор множества
# for user in users:
#     print(user)

# объединение множеств
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)

# Пересечение intersection или &
#Методы множества... - https://metanit.com/python/tutorial/3.4.php

users = frozenset({"Tom", "Bob", "Alice"})
user ="Tom"
users.remove(user)
print(users)
#ДЗ дописать код мини проекта СРМ система для хранения информации о сотруднике при помощи комплексного словаря