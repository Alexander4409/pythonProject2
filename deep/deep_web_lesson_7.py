#Дмитрий Лавреньтьев дать комментарий по коду
# Параллелизм
#Разница потоков и процессов
'''Поток thread делит выделенную память ядру процессора,
а также его процессорное время со всеми другими потоками,
которые создаются программой в рамках одного ядра процессора.
Программы на языке Python имеют, по умолчанию, один основной поток.
Можно создать их больше и позволить Python переключаться между ними.
Это переключение происходит очень быстро и кажется, что они работают параллельно.'''
from turtledemo.penrose import start

'''multiprocessing - представляет собой также независимую последовательность 
выполнения вычислений. В отличие от потоков threading, процесс имеет собственное ядро и 
следовательно выделенную ему память, которое не используется совместно с другими процессами. 
Процесс может клонировать себя, создавая два или более экземпляра в одном ядре процессора.'''

#GIL Global Interpreter Lock. Гарантирует, что в любой момент времени работает только один поток.

#демонстрация не правильной работы потока данных

# num = 2
#
#
# def thread_1():
#     global num
#     num += 2
#
# def thread_2():
#     global num
#     num *= 3
#
#
# print(thread_1())
# print(thread_2())

#Исследование разных потоков параллельного вычисления python
# import time
#
# def heavy(n):
#     for x in range(1,n):
#         for y in range(1,n):
#             x**y
#
# def sequence(n):
#     for i in range(n):
#         heavy(500)
#     print(f"{n} cycle compleat")
#
# if __name__ == "__main__":
#     start = time.time()
#     sequence(80)
#     end = time.time()
#     print(" All time program work", end - start)

#использование потоков


# import threading
# import time
#
#
# def heavy(n, i, thead):
#     for x in range(1, n):
#         for y in range(1, n):
#             x ** y
#     print(f"Цикл № {i}. Поток {thead}")
#
#
# def sequential(calc, thead):
#     print(f"Запускаем поток № {thead}")
#     for i in range(calc):
#         heavy(500, i, thead)
#     print(f"{calc} циклов вычислений закончены. Поток № {thead}")
#
#
# def threaded(theads, calc):
#     # theads - количество потоков
#     # calc - количество операций на поток
#
#     threads = []
#
#     # делим вычисления на `theads` потоков
#     for thead in range(theads):
#         t = threading.Thread(target=sequential, args=(calc, thead))
#         threads.append(t)
#         t.start()
#
#     # Подождем, пока все потоки
#     # завершат свою работу.
#     for t in threads:
#         t.join()
#
#
# if __name__ == "__main__":
#     start = time.time()
#     # разделим вычисления на 4 потока
#     # в каждом из которых по 20 циклов
#     threaded(4, 20)
#     end = time.time()
#     print("Общее время работы: ", end - start)

# Имитация однопоточного режима работы
#
# import threading
# import time
#
# def heavy():
#     # имитации операций ввода-вывода
#     time.sleep(2)
#
# def threaded(theads):
#     threads = []
#
#     # делим операции на `theads` потоков
#     for thead in range(theads):
#         t = threading.Thread(target=heavy)
#         threads.append(t)
#         t.start()
#
#     # Подождем, пока все потоки
#     # завершат свою работу.
#     for t in threads:
#         t.join()
#     print(f"{theads} циклов имитации операций ввода-вывода закончены")
#
# if __name__ == "__main__":
#     start = time.time()
#     # 80 потоков - это неправильно и показано
#     # чисто в демонстрационных целях
#     threaded(80)
#     end = time.time()
#     print("Общее время работы: ", end - start)


#Использование многопроцессорной обработки multiprocessing.
import multiprocessing
import time


def heavy(n, i, proc):
    for x in range(1, n):
        for y in range(1, n):
            x ** y
    print(f"Цикл № {i} ядро {proc}")


def sequential(calc, proc):
    print(f"Запускаем поток № {proc}")
    for i in range(calc):
        heavy(500, i, proc)
    print(f"{calc} циклов вычислений закончены. Процессор № {proc}")


def processesed(procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядро

    processes = []

    # делим вычисления на количество ядер
    for proc in range(procs):
        p = multiprocessing.Process(target=sequential, args=(calc, proc))
        processes.append(p)
        p.start()

    # Ждем, пока все ядра
    # завершат свою работу.
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    # узнаем количество ядер у процессора
    n_proc = multiprocessing.cpu_count()
    # вычисляем сколько циклов вычислений будет приходится
    # на 1 ядро, что бы в сумме получилось 80 или чуть больше
    calc = 80 // n_proc + 1
    processesed(n_proc, calc)
    end = time.time()
    print(f"Всего {n_proc} ядер в процессоре")
    print(f"На каждом ядре произведено {calc} циклов вычислений")
    print(f"Итого {n_proc * calc} циклов за: ", end - start)

# Весь вывод показывать не будем
# ...
# ...
# ...
# Всего 6 ядер в процессоре
# На каждом ядре произведено 14 циклов вычислений
# Итого 84 циклов вычислений за: 5.0251686573028564


# https://docs-python.ru/tutorial/mnogopotochnost-python/
#https://habr.com/ru/articles/667630/