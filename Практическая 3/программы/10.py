#-- coding: utf-8 --


#Задание 10
K = int(input('Номер числа Фибоначчи:'))
N = int(input('Введите количество чисел Фибоначчи:'))
summ = 0
(x, y)  = (0, 1)
for i in range(1, K + N - 1):
 (x, y) = (y, x + y)
 if i >= K-1:
   summ += x
print('Сумма чисел Фибоначчи:',summ)