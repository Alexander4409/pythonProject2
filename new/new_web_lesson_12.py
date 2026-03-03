#Словари
# dict_1 = {"key":1}
#dictionary = { ключ1:значение1, ключ2:значение2, ....}

# users = {10:"Tom", 21:"Stasy", 20:"John",280:"Акакий"}
# key - возраст(числа), value - имя (Строка)
#
# emails = {"tom@mail.ru":"Tom", "Bill@gmail.ru":"Bill"}
# print(emails)

# user_list = [
#     ["+12345","Tom"],
#     ["+45234","Bob"],
#     ["+34242","Bill"]
# ]
#
# #Двойной индекс - print(user_list[2][1])
#
# users_dict = dict(user_list)
# print(users_dict)




users_dict = {
    '+12345': 'Tom',
    '+45234': 'Bob',
    '+34242': 'Bill'
}
# по ключу можем вытаскивать значения
# print(users_dict['+12345'])
# установка элемента
# users_dict['+45234'] = "Bob Smith"
# print(users_dict)
# users_dict["+53333"] = "Marta"
# print(users_dict)

# key = "+33333"
# if key in users_dict:
#     user = users_dict[key]
#     print(user)
# else:
#     print("Not found")
# получение значения по ключу при помощи get
# get(key) - возвращает из словаря элем. с ключем key в противном случае получаем None
# get(key,default) - возвращает из словаря элем. с ключем key в противном случае
# получаем значение по умолчанию

# user1 = users_dict.get("+12345")
# print(user1)
# user2 = users_dict.get("+77777", "Unknown user")
# print(user2)

#удаление по ключу при помощи del
# del users_dict['+34242']
#
# print(users_dict)
#
# #Удаление по ключу при помощи pop
# # pop(key) - удаляет из словаря элем. с ключем key в противном случае получаем None
# # pop(key,default) - удаляет из словаря элем. с ключем key в противном случае
# # получаем значение по умолчанию
# user = users_dict.pop('+12345')
# print(users_dict)

# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
# # Выводить словарь продуктов после какой-либо операции выбранной
# # пользователем либо по запросу пользователя
# # Удалять элементы
# # Получать какой-то конкретный элемент
# # Изменять значение у элемента
# # Добавить элемент
#
# while True:
#     user_input = int(input("1 - show product dictionary\n"
#                            "2 - delete element \n"
#                            "3 ..."))
#     if user_input == 1:
#         print(product_dict)
#
#     elif user_input == 5:
#         print("Bye bye")
#         break
#     else:
#         print("Try another one button ")

#Объединение 2 словарей в 1
# update()-
# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
#
# product = {'Milk':4}
#
# product_dict.update(product)
#
# print(product_dict)

#Перебор словаря
# product_dict = {"lemons":3,"Tomatoes":5,"Eggs":10}
#
# for key in product_dict:
#     print(f'product: {key}, Count: {product_dict[key]}')