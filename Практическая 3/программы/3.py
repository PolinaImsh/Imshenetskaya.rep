#Задание 3


#-- coding: utf-8 --
A = int(input('Введите число A(A>B):'))
B = int(input('Введите число B(A>B):'))
for i in range(A, B-1, -1):
  if i%2!=0:
    print (i)