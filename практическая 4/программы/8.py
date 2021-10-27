#-- coding: utf-8 --


#Задание 8
stroka = input('Строка:')
a = stroka[:stroka.find('h')] 
b = stroka[stroka.find('h'):stroka.rfind('h') + 1]
c = stroka[stroka.rfind('h') + 1:]
s = a + b[::-1] + c
print('Новая строка:',stroka)