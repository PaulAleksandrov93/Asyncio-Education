# import asyncio


# async def main():
#     print('Hello...')
#     await asyncio.sleep(1)
#     print('World!')

# asyncio.run(main())

# ===

# import asyncio

# async def task1():
#     await asyncio.sleep(1)
#     print("Задача 1 завершена")


# async def task2():
#     await asyncio.sleep(1)
#     print("Задача 2 завершена")


# async def main():
#     tasks = [task1(), task2()]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# ===

# import time
# import urllib.request

# # Список URL для загрузки
# urls = [
#     'http://www.python.org',
#     'http://www.python.org/about/',
#     'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
#     'http://www.python.org/doc/',
#     'http://www.python.org/download/',
#     'http://www.python.org/getit/',
#     'http://www.python.org/community/',
#     'https://wiki.python.org/moin/',
# ]

# start_time = time.time()

# # Загрузка каждого URL
# for url in urls:
#     print(f'Загрузка {url}')  # Выводим сообщение о загрузке URL
#     response = urllib.request.urlopen(url)
#     print(f'Загружено {url}')  # Выводим сообщение о завершении загрузки URL

# end_time = time.time()
# # Выводим общее время загрузки
# print(f'Загружено {len(urls)} URL за {end_time - start_time} секунд')  

# ===

# import time


# # Функция для вычисления факториала
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# start_time = time.time()

# # Вычисление факториала для каждого числа от 1 до 20
# for i in range(1, 21):
#     print(f'Факториал {i} = {factorial(i)}')  # Выводим факториал числа

# end_time = time.time()
# # Выводим общее время вычисления
# print(f'Вычислено 20 факториалов за {end_time - start_time} секунд')  

# ===

# import asyncio
# import random

# class Pizzeria:
#     def __init__(self, name):
#         self.name = name

#     async def make_pizza(self, order_id):
#         cook_time = random.randint(2, 5)      # случайное время готовки пиццы от 2 до 5 секунд
#         print(f'Пиццерия {self.name} начала готовить пиццу для заказа {order_id}.')
#         await asyncio.sleep(cook_time)        # ожидание пока пицца готовится
#         print(f'Пиццерия {self.name} закончила готовить пиццу для заказа {order_id}.')

# async def main():
#     pizzeria = Pizzeria("Тесто & Сыр")

#     # создание 5 заказов
#     tasks = [pizzeria.make_pizza(i) for i in range(1, 6)]

#     # запуск всех задач (заказов) в Event Loop
#     await asyncio.gather(*tasks)

# # запуск Event Loop
# asyncio.run(main())

# ===

# import asyncio

# # Определение корутины
# async def my_coroutine():
#     print("Запуск корутины")
#     await asyncio.sleep(1)  # Приостановка корутины на 1 секунду
#     print("Завершение корутины")

# # Создание задачи из корутины
# async def main():
#     task = asyncio.create_task(my_coroutine())
#     await task

# # Запуск event loop
# asyncio.run(main())

# ===

# import asyncio

# # Определение асинхронной функции (корутины) cook_dish(n), которая имитирует повара, готовящего блюдо.
# # Используется корутина для того, чтобы одновременно запускать несколько "поваров" и использовать время ожидания (приготовление) эффективно.

# async def cook_dish(n):
#     print(f"Повар {n} начинает готовить")       # Повар n начинает готовить
#     await asyncio.sleep(n)                      # Повар готовит блюдо n секунд. asyncio.sleep(n) используется для имитации задержки, которая требуется для приготовления блюда.
#     print(f"Повар {n} закончил готовить")       # Повар n закончил готовить
#     return f"Блюдо от повара {n}"               # Возвращает строку, указывающую, что блюдо от повара n готово.

# # Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
# async def main():
#     tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)]  # Создаются задачи для каждого повара (от 1 до 3). Используется create_task для запуска корутины.
#     print(await asyncio.gather(*tasks))                               # Ожидает завершения всех задач, затем выводит результат. asyncio.gather используется для ожидания всех корутин, затем собирает их результаты в список.

# # Запуск главной корутины
# asyncio.run(main())  

# ===

# import asyncio
# import random

# async def boil_water(time: int):
#     print('Ставим чайник с водой на плиту...')
#     await asyncio.sleep(time)                               # Передаем управление плите
#     print('Чайник закипел!')

# async def chop_vegetables():
#     print('Начинаем нарезать овощи...')
#     await asyncio.sleep(random.randint(2, 4))               # Передаем управление нарезке овощей
#     print('Овощи нарезаны!')

# async def prepare_dinner():
#     await asyncio.gather(boil_water(5), chop_vegetables())   # Запускаем задачи параллельно


# asyncio.run(prepare_dinner())

# ===

# import aiohttp                                       
# import asyncio                                       

# async def fetch_data(url):                           # Определяем асинхронную функцию для получения данных с указанного URL
#     async with aiohttp.ClientSession() as session:   # Создаем асинхронную сессию HTTP запросов, используя модуль aiohttp для оптимального управления ресурсами
#         async with session.get(url) as response:     # Осуществляем асинхронный GET запрос к URL, чтобы не блокировать выполнение других операций
#             return await response.text()             # Возвращаем текстовые данные ответа, используем await, чтобы дождаться полного получения данных

# async def main():                                    # Определяем асинхронную функцию, которая будет запускаться при выполнении программы
#     data = await fetch_data('http://python.org')     # Получаем данные с сайта python.org, используем await, чтобы дождаться получения данных
#     print(data)                                      # Выводим полученные данные

# asyncio.run(main())                                  # Запускаем асинхронную функцию main(), используя asyncio.run для создания и выполнения нового событийного цикла

# ===

# import asyncio                                      

# async def cook_pasta():                             # Определяем асинхронную функцию для приготовления пасты
#     print("Начинаем готовить пасту")                # Выводим сообщение о начале приготовления пасты
#     await asyncio.sleep(5)                          # Используем asyncio.sleep для эмуляции времени приготовления пасты. Await приостанавливает выполнение функции на 5 секунд, не блокируя выполнение других асинхронных операций 
#     print("Паста готова")                           # После "ожидания" 5 секунд выводим сообщение о том, что паста готова

# async def main():                                   # Определяем асинхронную функцию, которая будет запускаться при выполнении программы
#     await cook_pasta()                              # Запускаем функцию приготовления пасты и ожидаем ее завершения с использованием await

# asyncio.run(main())                                 # Запускаем асинхронную функцию main(), используя asyncio.run для создания и выполнения нового событийного цикла

# ===

# import asyncio                                     

# async def cook_pasta():                            # Определяем асинхронную функцию для приготовления пасты
#     print("Начинаем готовить пасту")               # Выводим сообщение о начале приготовления пасты
#     await asyncio.sleep(5)                         # Используем asyncio.sleep для эмуляции времени приготовления пасты. Await приостанавливает выполнение функции на 5 секунд, не блокируя выполнение других асинхронных операций
#     print("Паста готова")                          # После "ожидания" 5 секунд выводим сообщение о том, что паста готова

# async def cook_sauce():                            # Определяем асинхронную функцию для приготовления соуса
#     print("Начинаем готовить соус")                # Выводим сообщение о начале приготовления соуса
#     await asyncio.sleep(3)                         # Используем asyncio.sleep для эмуляции времени приготовления соуса. Await приостанавливает выполнение функции на 3 секунды, не блокируя выполнение других асинхронных операций
#     print("Соус готов")                            # После "ожидания" 3 секунд выводим сообщение о том, что соус готов

# async def main():                                  # Определяем асинхронную функцию, которая будет запускаться при выполнении программы
#     await asyncio.gather(cook_pasta(), cook_sauce()) # Используем asyncio.gather для запуска двух корутин одновременно и ожидания их завершения. Await приостанавливает выполнение функции до тех пор, пока не будут завершены обе корутины

# asyncio.run(main())                                # Запускаем асинхронную функцию main(), используя asyncio.run для создания и выполнения нового событийного цикла

# ===

# import aiohttp                                    
# import asyncio                                    

# async def fetch_data(url):                        # Определяем асинхронную функцию для загрузки данных с указанного URL
#     async with aiohttp.ClientSession() as session: # Создаем асинхронную сессию HTTP. Используем асинхронный контекстный менеджер для автоматического закрытия сессии после выполнения запросов
#         async with session.get(url) as response:  # Отправляем асинхронный GET-запрос к указанному URL. Используем асинхронный контекстный менеджер для автоматического закрытия соединения после получения ответа
#             return await response.text()           # Возвращаем текстовое содержимое ответа. Await используется для ожидания получения всего содержимого ответа

# async def main():                                  # Определяем асинхронную функцию, которая будет запускаться при выполнении программы
#     data = await fetch_data('http://python.org')   # Загружаем данные с сайта python.org. Await используется для ожидания завершения загрузки данных
#     print(data)                                    # Выводим загруженные данные

# asyncio.run(main())                                # Запускаем асинхронную функцию main(), используя asyncio.run для создания и выполнения нового событийного цикла

# ===

# import asyncio

# async def task1():
#     await asyncio.sleep(1)
#     print("Привет из корутины task1")

# async def task2():
#     await asyncio.sleep(1)
#     print("Привет из корутины task2")

# async def main():
#     await asyncio.create_task(task1())
#     await asyncio.create_task(task2())

# asyncio.run(main())

# ===

# import asyncio


# async def task1():
#     print("Начинаем задачу 1")
#     await asyncio.sleep(1)
#     print("Привет из корутины task1")
#     await asyncio.sleep(1)
#     print("Задача 1 завершилась")


# async def task2():
#     print("Начинаем задачу 2")
#     await asyncio.sleep(2)
#     print("Привет из корутины task2")
#     await asyncio.sleep(2)
#     print("Задача 2 завершилась")


# async def task3():
#     print("Начинаем задачу 3")
#     await asyncio.sleep(3)
#     print("Привет из корутины task3")
#     await asyncio.sleep(3)
#     print("Задача 3 завершилась")


# async def main():
#     task_1 = asyncio.create_task(task1())
#     task_2 = asyncio.create_task(task2())
#     task_3 = asyncio.create_task(task3())

#     await asyncio.gather(task_1, task_2, task_3)
# asyncio.run(main())

# ===

# import asyncio


# async def my_coroutine(duration):
#     print("Starting my_coroutine")
#     await asyncio.sleep(duration)
#     print("Finishing my_coroutine")
#     return "Result"

# asyncio.run(my_coroutine(5))

# ===

# import asyncio                          

# async def first_coroutine(duration):    # Объявляем первую корутину, которая принимает в качестве аргумента продолжительность ожидания
#     print("Начинаем first_coroutine")   # Выводим информационное сообщение о начале выполнения первой корутины
#     await asyncio.sleep(duration)       # Приостанавливаем выполнение текущей корутины на указанное количество секунд. 
#                                         # asyncio.sleep используется для имитации длительной операции
#     print("Завершаем first_coroutine")  # Выводим информационное сообщение о завершении выполнения первой корутины
#     return "Результат 1"                # Возвращаем результат выполнения первой корутины

# async def second_coroutine(duration):   # Объявляем вторую корутину, аналогичную первой, с таким же аргументом
#     print("Начинаем second_coroutine")  # Выводим информационное сообщение о начале выполнения второй корутины
#     await asyncio.sleep(duration)       # Аналогично первой корутине, приостанавливаем выполнение на указанное время
#     print("Завершаем second_coroutine") # Выводим информационное сообщение о завершении выполнения второй корутины
#     return "Результат 2"                # Возвращаем результат выполнения второй корутины

# async def main():
#     result1, result2 = await asyncio.gather(first_coroutine(5), second_coroutine(3))
#     print("Результат 1:", result1)
#     print("Результат 2:", result2)


# asyncio.run(main()) 

# ===

# import asyncio


# async def main():
#     print("Hello, Asyncio!")

# asyncio.run(main())

# ===

# import asyncio


# async def coro_1():
#     await asyncio.sleep(1)
#     return "coro_1 says, hello coro_2!"


# async def coro_2():
#     await asyncio.sleep(2)
#     return "coro_2 says, hello coro_1!"


# async def main():
#     ret1, ret2 = await asyncio.gather(coro_1(), coro_2())
#     print(ret1)
#     print(ret2)
    

# asyncio.run(main())

# ===

# import asyncio 


# async def generate(n):
#     print(f'Корутина generate с аргументом {n}')


# async def main():
#     # создание 10 задач
#     tasks = [generate(i) for i in range(10)]
#     # запуск всех задач (заказов) в Event Loop
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# ===

# import asyncio


# async def coro_1():
#     print("Вызываю корутину 0")


# async def coro_5():
#     print("Вызываю корутину 3")
#     await coro_3()


# async def coro_3():
#     print("Вызываю корутину 2")
#     await coro_2()


# async def coro_4():
#     print("Вызываю корутину 1")
#     await coro_1()


# async def coro_2():
#     print("Вызываю корутину 4")
#     await coro_4()


# asyncio.run(coro_5())

# ===

# import asyncio                 

# async def my_coroutine():                        # Определяем асинхронную функцию (корутину)
#     await asyncio.sleep(1)                       # Приостанавливаем выполнение этой корутины на 1 секунду. Мы используем этот метод для имитации какой-либо асинхронной операции
#     print("Задача выполнена")                    # Выводим сообщение об окончании выполнения задачи 

# async def main():                                # Определяем основную асинхронную функцию
#     task = asyncio.create_task(my_coroutine())   # Создаем задачу из корутины. Этот метод позволяет начать выполнение корутины и возвращает объект Task, который можно ожидать
#     await task                                   # Ожидаем выполнения задачи. Благодаря этому код будет ждать выполнения задачи, прежде чем завершиться

# asyncio.run(main())            # Запускаем главную асинхронную функцию. Это удобный способ запустить корутину на верхнем уровне, он создает новый событийный цикл и закрывает его

# ===

# import asyncio

# async def coro_1():
#     await asyncio.sleep(1)
#     print('Coroutine 1 is done')


# async def coro_2():
#     await asyncio.sleep(2)
#     print('Coroutine 2 is done')


# async def coro_3():
#     await asyncio.sleep(3)
#     print('Coroutine 3 is done')


# async def main():
#     task1 = asyncio.create_task(coro_1())
#     task2 = asyncio.create_task(coro_2())
#     task3 = asyncio.create_task(coro_3())
#     await asyncio.gather(task1, task2, task3)

# asyncio.run(main())

# ===

# import asyncio

# async def coro(n):
#     print(f'Coroutine {n} is done')
#     await asyncio.sleep(1)

# async def main():
#     tasks = [coro(i) for i in range(10)]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# ===

import asyncio

# Словарь максимальных значений счетчиков
max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

# Словарь для хранения текущих значений счетчиков
counters = {counter: 0 for counter in max_counts}

# Асинхронная функция counter
async def counter(counter_name, delay):
    while counters[counter_name] < max_counts[counter_name]:
        # Увеличиваем значение счетчика на 1
        counters[counter_name] += 1
        # Выводим текущее значение счетчика
        print(f"{counter_name}: {counters[counter_name]}")
        # Ждем указанное количество секунд
        await asyncio.sleep(delay)

# Асинхронная функция main
async def main():
    # Создаем две задачи для счетчиков с разными именами и одинаковой задержкой
    task1 = asyncio.create_task(counter("Counter 1", 1))
    task2 = asyncio.create_task(counter("Counter 2", 1))
    
    # Ожидаем завершения обеих задач
    await asyncio.gather(task1, task2)

# Запускаем асинхронную программу
asyncio.run(main())
