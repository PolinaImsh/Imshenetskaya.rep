#-- coding: utf-8 --


#Задание 9
n = int(input('Введите количество чисел Фибоначчи:'))
summ = 0
(x, y)  = (0, 1)
for i in range(1, n):
 (x, y) = (y, x + y)
 summ += x
print('Сумма чисел Фибоначчи:',summ)