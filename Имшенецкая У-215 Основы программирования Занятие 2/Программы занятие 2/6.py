str1 = int(input("Cтрока первой клетки:"))
stolbec1 = int(input("Столбец первой клетки:"))
str2 = int(input("Строки второй клетки:"))
stolbec2 = int(input("Столбец второй клетки:"))

if ((str1 and stolbec1) >= 1 and (str1 and stolbec1) <= 8) and ((str2 and stolbec2) >= 1 and (str2 and stolbec2) <= 8):
    if (str1 % 2 == 1 and stolbec1 % 2 == 1) or (str1 % 2 == 0 and stolbec1 % 2 == 0) :
        colour1 = str("White")
    else:
        colour1 = str("Black")
    if (str2 % 2 == 1 and stolbec2 % 2 == 1) or (str2 % 2 == 0 and stolbec2 % 2 == 0):
        colour2 = str("White")
    else:
        colour2 = str("Black")
else:
  print("Cовпадают ли цвета? - ")
if colour1 == colour2:
    print("Да, совпадают")
else:
    print("Нет, не совпадают")