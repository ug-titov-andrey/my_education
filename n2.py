'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.'''
second = int(input('Введите время в секундах - '))
hour = second//3600
out_second = second%3600
min = out_second//60
out_second=out_second%60
#print(hour,min,out_second)

print('Время в формате часы:минуты:секунды равно => %d:%-2d:%-2d'%(hour,min,out_second))