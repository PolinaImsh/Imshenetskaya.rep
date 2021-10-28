#-- coding: utf-8 --


#Задание 5
sum = 0
n = int(input('Введите число n:'))
for i in range(n+1):
  m = i ** 3
  sum += m
print('Резельтат:', sum)