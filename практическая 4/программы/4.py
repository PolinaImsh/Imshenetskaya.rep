#-- coding: utf-8 --


#Задание 4
s = input('Строка:')
one = s[:s.find(' ')]
two = s[s.find(' ') + 1:]
print('Новая строка:', two + ' ' + one)