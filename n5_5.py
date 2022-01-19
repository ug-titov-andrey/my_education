'''5. Создать (программно) текстовый файл,
записать в него программно набор чисел,
 разделённых пробелами.
  Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''
import random, functools
num = 3
numbers_gen=(round(100*random.random(),3) for s in range(num))
file_name = 'user_data5.txt'
with open(file_name, 'w+') as f:
    for numb_data in numbers_gen:
        f.write(str(numb_data)+' ')
    f.seek(0)
    inp_list = f.readline().split()
    sum = functools.reduce(lambda x,y: float(x)+float(y), inp_list)
print(f'Сумма  последовательности случайных чисел равна => {sum}')






