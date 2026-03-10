#Словари 2 урок
# items()

# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
# for key, value in product_dict.items():
#      print(f'product: {key}, Count: {value}')

# получение только ключей из словаря
# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
#
# for key in product_dict.keys():
#      print(f'product: {key}')

# получение только значений
# for value in product_dict.values():
#     print(f"Count {value}")

# комплексные словари
# users = {
#     "Tom": {
#         "phone": "+971478745",
#         "email": "tom12@gmail.com"
#     },
#     "Bob": {
#         "phone": "+876390444",
#         "email": "bob@gmail.com",
#         "skype": "bob123"
#     }
# }
#
# # get_email = users["Tom"]["email"]
# # print(get_email)
#
# bob_skype = users["Bob"].get("skype","No Data")
# print(bob_skype)

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
# print(products_catalog)
#
# name = input("product name")
# calories = int(input("enter calories"))
# count = int(input("enter count"))
#
# products_catalog[name] = {
#     "calories_per_100g":calories,
# "items_in_package":count
# }
# print(products_catalog)

################################### Множества set() ###################################
# users = ["Bob", "Alice", "Mike", "Bob", "Tom", "Tom", "Billy"]
# print(users)
# #преобразование списка в множество
# people = set(users)
# print(people)

# Функции и методы множества

# add - добавление элемента
# users = {"Bob", "Alice", "Mike", "Bob", "Tom", "Tom", "Billy"}
# users.add("Sam")
# print(users)

# remove() - удалить элемент
# users.remove("Bob")
# print(users)

# объединение множеств - union
# users = {"Bob", "Alice", "Mike"}
# users_2 = {"Tom", "Bob", "Billy"}

# all_users = users.union(users_2)
# print(all_users)
# логическое сложение
# print(users | users_2)

#пересечение множеств
# &, intersection()
# all_us = users.intersection(users_2)
# print(all_us)

#https://metanit.com/python/tutorial/3.4.php

#Frosen_set - не изменяемая коллекция

# users = frozenset({"Bob", "Alice", "Mike", "Bob", "Tom", "Tom", "Billy"})
#
# print("Tom" in users)


#ДЗ дописать код мини проекта СРМ система для хранения информации о сотруднике при помощи комплексного словаря
