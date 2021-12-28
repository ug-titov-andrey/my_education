'''Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
на своем месте. Для заполнения списка элементов необходимо использовать функцию input().'''
my_list=[]
while True:
    tp_inp=input('Введите значения. Для выхода нажмите q:  ')
    if tp_inp=='q':
        break
    my_list.append(tp_inp)
print(my_list)
for ind in range(0,len(my_list)-1,2):
    my_list[ind],my_list[ind+1] =my_list[ind+1],my_list[ind]
print(my_list)
