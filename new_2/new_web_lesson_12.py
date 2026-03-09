#Словари - dict
# users = {14:"Tom", 12:"Mary", 21:"Barbara", 34:"Jerry"}
# print(users)
# ключ - email, значение - имя пользователя
# emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}
# не обязательно чтобы ключ был такого же типа данных, как и его значение
# objects = {1: "Tom", "2": True, 3: 100.6}


# Преобразование списка в словарь
#Двумерный список
# users = [["+12345","Tom"],
#          ['+54321',"Mary"],
#          ["+15243","Bob"]
#          ]
# #Получение конкретного элемента из двумерного списка
# print(users[2][1])
# #Преобразование двумерного списка в словарь
# users_dict = dict(users)
# print(users_dict)

# users_dict = {
#     '12345': 'Tom',
#     '54321': 'Mary',
#     '15243': 'Bob'
# }
# print(users_dict)
# #Получение элемента по ключу
# print(users_dict["12345"])
# #Изменение значение по ключу
# users_dict["54321"] = "Stacy"
# print(users_dict)
# Добавление элемента
# users_dict["09898"] = "Robert"
# print(users_dict)

# key = "12345"
# if key in users_dict:
#     user = users_dict[key]
#     print(user)
# else:
#     print("Not found")

#get для получения элементов
# get(key)
# get(key,default)

# users_dict = {
#     '12345': 'Tom',
#     '54321': 'Mary',
#     '15243': 'Bob'
# }
# print(users_dict)
#
# user = users_dict.get("1234444", "Unknown user")
# print(user)


# Удаление элемента del

# users_dict = {
#     '12345': 'Tom',
#     '54321': 'Mary',
#     '15243': 'Bob'
# }
# print(users_dict)

# del users_dict["54321eee"]
# print(users_dict)

#Удаление при помощи pop()
# pop(key)
# pop(key,default)

# key = '15243'
# user = users_dict.pop(key,"unknown user ")
# print(user)
# print(
#     users_dict
# )

# Добавление элементов в словарь
users_dict = {
    '12345': 'Tom',
    '54321': 'Mary',
    '15243': 'Bob'
}
print(users_dict)

# add_user = {"102938":"John"}
#
# users_dict.update(add_user)
#
# print(users_dict)

# Перебор словарей


for key in users_dict:
    print(f'Phone: {key}, User: {users_dict[key]}')

#ДЗ продуктовая корзина
# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
# # Выводить словарь продуктов после какой-либо операции выбранной
# # пользователем либо по запросу пользователя
# # Удалять элементы
# # Получать какой-то конкретный элемент
# # Изменять значение у элемента
# # Добавить элемент
