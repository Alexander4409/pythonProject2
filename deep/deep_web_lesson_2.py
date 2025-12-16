'''
1 изменяемые типы данных
списки, словари, множества, байтовый массив
2 не изменяемые типы данных
кортежи, float, int, str, bool, None, complex, bytes, frozen set
'''
#
# g = None
# print(type(g))
#функция проверки ячеек памяти и понимания что такое переменная
#Ps переменная эта ссылка на ячейку памяти
# def heap_test_foo() -> None:
#     num = 100
#     num_2 = num
#
#     print(f'num: id {id(num)}')
#     print(f'num_2: id {id(num_2)}')
#
# # num: id 140707403497352
# # num_2: id 140707403497352
#
# heap_test_foo()
# поменяли переменную
# def heap_test_foo() -> None:
#     num = 100
#     num_2 = num
#     print(f'num: id {id(num)}')
#     print(f'num_2: id {id(num_2)}')
#     num += 1
#     print(f'num: id {id(num)}')

# num: id 140707397271432
# num_2: id 140707397271432
# num: id 140707397271464

# heap_test_foo()

#поведение изменяемых типов данных
# def heap_test_foo() -> None:
#     lst_num = [100]
#     lst_num_2 = lst_num
#     print(f'lst_num: id {id(lst_num)}')
#     print(f'lst_num_2: id {id(lst_num_2)}')
#     lst_num.append(101)
#     print(f'lst_num: id {id(lst_num)}')
#     print(f'lst_num_2: id {id(lst_num_2)}')
#
# heap_test_foo()

# lst_num: id 2361271800000
# lst_num_2: id 2361271800000
# lst_num: id 2361271800000
# lst_num_2: id 2361271800000

# https://habr.com/ru/articles/825806/

#плохой пример
# def test_foo_1(listing=[]) -> None:
#     listing.append(1)
#     print(listing)
#
# test_foo_1()
# # [1]
# test_foo_1()
# # [1, 1]
# test_foo_1([652,435])
# #[652, 435, 1]
# test_foo_1()
# #[1, 1, 1]

#хороший пример
# def test_foo_2(listing = None) ->None:
#     if listing is None:
#         listing = []
#     listing.append(1)
#     print(listing)
#
# test_foo_2()
# #[1]
# test_foo_2()
# #[1]
# test_foo_2([8,24,6,2])
# #[8, 24, 6, 2, 1]
# test_foo_2()
#https://ru.stackoverflow.com/questions/1032284/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-pycharm-github