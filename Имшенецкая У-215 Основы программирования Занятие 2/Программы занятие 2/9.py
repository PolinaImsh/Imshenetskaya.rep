print('Введите длину первой стороны шоколадки в дольках n, (n не равна m)')
n = int(input())
print('Введите длину второй стороны шоколадки в дольках m, (n не равна m)')
m = int(input())
print('Оставшаяся часть в дольках k')
k = int(input())
if n != m:
    if (n * m > k) and  (k % n == 0 or k % m == 0):
        print("Да")
    else:
        print("Нет")
else:
    print("Шоколадка должна быть прямоугольной формы")
