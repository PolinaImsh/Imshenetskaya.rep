#-- coding: utf-8 --


#Задание 7
a = input('Строка:')
a = a[:a.find('h')] + a[a.rfind('h') + 1:]
print('Новая строка:', a)