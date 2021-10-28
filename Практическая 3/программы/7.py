#-- coding: utf-8 --


#Задание 7
fact = 1
sum = 0
n = int(input('Введите число n:'))
for i in range(1, n+1):
  fact *= i
  sum += fact
print('Сумма факториалов:', sum)