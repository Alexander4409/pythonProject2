#Корутина - сопрограмма
#Футура - фьючерс
#Таск - Задача
# обычные функции работающие в не асинхронном режиме, работа занимает 6 секунд.
# Последовательность выполнения стандартная

# import time
#
# def func_1(x):
#     print(x**2)
#     time.sleep(3)
#     print(f"работа {func_1.__name__} завершена!")
#
#
# def func_2(x):
#     print(x**3)
#     time.sleep(3)
#     print(f"работа {func_2.__name__} завершена!")
#
#
# def main():
#     func_1(2)
#     func_2(2)
#
# print(time.strftime("%X"))
#
# main()
#
# print(time.strftime("%X"))

#Асинхронное выполнение

# import time
# import asyncio
#
# async def func_1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_1.__name__} завершена!")
#
#
# async def func_2(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print(f"работа {func_2.__name__} завершена!")
#
#
# async def main():
#     task_1 = asyncio.create_task(func_1(3))
#     task_2 = asyncio.create_task(func_2(4))
#
#     await task_1
#     await task_2
#
# print(time.strftime("%X"))
#
# asyncio.run(main())
#
# print(time.strftime("%X"))


# Асинхронные функции и корутины
# получение типов функций
# import time
#
# def func_1(x):
#     print(x**2)
#     time.sleep(3)
#     print(f"работа {func_1.__name__} завершена!")
#
#
# def func_2(x):
#     print(x**3)
#     time.sleep(3)
#     print(f"работа {func_2.__name__} завершена!")
#
#
# def main():
#     func_1(2)
#     func_2(2)
#
# print(type(func_1(2)))
# print(type(func_2))

# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(type(fun1))
#
# print(type(fun1(4)))

#return: Завершает функцию, возвращает одно значение, состояние теряется.
#yield: Приостанавливает функцию, может возвращать несколько значений
# (по одному), состояние сохраняется.

#Генераторская функция
# def count_up_to(num):
#     count = 1
#     while count <= num:
#         yield count #приостановка функции
#         count += 1
#
#
# # Создание объекта генератора
# counter = count_up_to(10)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# Футуры и задачи