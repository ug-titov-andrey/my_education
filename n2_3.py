'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.'''
list_season=['зима','зима', 'весна','весна','весна', 'лето','лето','лето','осень','осень','осень','зима',]
dict_season={ 1:'зима',2:'зима', 3:'весна',4:'весна',5:'весна', 6:'лето',7:'лето',8:'лето', 9:'осень', 10:'осень', 11:'осень',12:'зима'}
while True:
     number_month = input('Введите целое число от 1 до 12. Для выхода нажмите q:  ')
     if number_month == 'q': break
     try:
          number_season = int(number_month) - 1
     except
     try:
          number_season = int(number_month)-1
          print(f'Сейчас {list_season[number_season]}')
     except:
          print('Введите правильный номер месяца\n ____________________________')

while True:
     number_month = input('Введите целое число от 1 до 12. Для выхода нажмите q:  ')
     if number_month  == 'q': break
     try:
          number_season = int(number_month)
          print(f'Сейчас {dict_season[number_season]}')
     except:
          print('Введите правильный номер месяца\n_____________')






