print('Введите переменную "sekonds"')
sekonds=input()
minuts=int(sekonds)/60
hour=int(minuts)/60
days=int(hour)/24
print('дни:часы:минуты:секуны')
print(days,':',hour,':', minuts,':',sekonds)