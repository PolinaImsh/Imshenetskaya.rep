#-- coding: utf-8 --


#Задание 6
fact = 1
n = int(input('Введите число n:'))
for i in range(1, n+1):
  fact *= i
print('Факториал:',fact)