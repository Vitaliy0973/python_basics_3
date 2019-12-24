# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.

# the_list = [1, 0.4, 'The world', None, True, (1, 2, 3)]
# for i in the_list:
#     print(f'Элемент {i} имеет тип {type(i)}.')


# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При
# нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию
# input().

# new_list = []
# while True:
#     element = input('Введите элемент списка. Что-бы остановить введите "q": ')
#     if element == 'q':
#         break
#     new_list.append(element)
# print(f'Список - {new_list}')
# i = 1
# while i < len(new_list):
#     x = new_list.pop(i)
#     new_list.insert((i-1), x)
#     i += 2
# print(f'Новый список - {new_list}')


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# seasons_list = ['зима', 'весна', 'лето', 'осень']
# seasons_dict = {
#     'зима': [12, 1, 2],
#     'весна': [3, 4, 5],
#     'осень': [9, 10, 11],
#     'лето': [6, 7, 8],
# }
# while True:
#     answer = input('Решение через list, введите "1". Через dict, введите "2". Что-бы выйти введите "q". ')
#     if answer == 'q':
#         break
#     elif answer == '1':
#         while True:
#             user_number = input('Введите номер месяца. Что-бы выйти нажмите "q" ')
#             try:
#                 if int(user_number) < 3 or int(user_number) == 12:
#                     print(f'{user_number} - {seasons_list[0]}')
#                 elif 3 <= int(user_number) < 6:
#                     print(f'{user_number} - {seasons_list[1]}')
#                 elif 6 <= int(user_number) < 9:
#                     print(f'{user_number} - {seasons_list[2]}')
#                 elif 9 <= int(user_number) < 12:
#                     print(f'{user_number} - {seasons_list[3]}')
#                 else:
#                     print('Не верный ввод. Повторите попытку.')
#             except ValueError as e:
#                 if user_number == 'q':
#                     break
#                 else:
#                     print('Не верный ввод. Повторите попытку.')
#     elif answer == '2':
#         while True:
#             user_number = input('Введите номер месяца. Что-бы выйти нажмите "q" ')
#             try:
#                 user_number = int(user_number)
#                 for key, value in seasons_dict.items():
#                     if user_number in value:
#                         print(f'{user_number} - {key}')
#             except ValueError as e:
#                 if user_number == 'q':
#                     break
#                 else:
#                     print('Не верный ввод. Повторите попытку.')


# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# text = input('Введите несколько слов разделяя их пробелами: ')
# the_new_list = text.split()
# number = 1
# for i in the_new_list:
#     if len(i) > 10:
#         word = i
#         print(f'{number}. {word[0:10]}')
#     else:
#         print(f'{number}. {i}')
#     number += 1


# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться
# после них.

# my_list = [7, 5, 3, 3, 2]
# my_list.sort(reverse=True)
# print()
# print((my_list))
# while True:
#     user_value = int(input('Введите натуральное число:  '))
#     if user_value in my_list:
#         if my_list.count(user_value) >= 1:
#             number = my_list.index(user_value) + my_list.count(user_value)
#             my_list.insert(number, user_value)
#     else:
#         my_list.append(user_value)
#         my_list.sort(reverse=True)
#     print(my_list)

