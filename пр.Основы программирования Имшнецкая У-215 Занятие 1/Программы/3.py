print('Введите своё имя')
name=input('')
print('Введите свой возраст')
age=int(input())
if (age > 0) and (age < 75) and(name != 'Иван'):
  if (age >= 16):
      print('Поздравляем, вы поступили во ВГУИТ!')
  else: 
     if (age < 16):
       print('Сначала нужно окончить школу!')
       print('Вам осталось учиться в школе')
       print(16- age, 'лет')
else:
  if(name=='Иван'): 
    print('Ошибка')