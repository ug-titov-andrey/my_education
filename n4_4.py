'''Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]'''
import random
if __name__=='__main__':
    inp_list = []
    numb = 50  # длина входного списка
    for ind in range(numb):
        inp_list.append(random.randint(0, 100))
    print(f'Исходный список {inp_list}')



    out_list=[value for  ind,value in enumerate(inp_list) if  value not in inp_list[:ind] + inp_list[(ind+1):] ]
    #a= [inp_list[:ind] + inp_list[(ind+1):] for  ind,value in enumerate(inp_list) ]
    print(f'Отсортированный список {out_list}')

