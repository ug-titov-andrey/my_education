''' Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
  в новый текстовый файл.
'''
str_out=''
file_name_en='data_for_4.txt'
file_name_r='user_data5.txt'
templ_list=['Один', 'Два', 'Три', 'Четыре']
orig_list=['One', 'Two', 'Three', 'Four']
with  open(file_name_en, 'r', encoding='UTF-8') as f:
    for ind,f_str in enumerate(f):
        str_out+=f_str.replace(orig_list[ind],templ_list[ind])
f = open(file_name_r, 'w',encoding='UTF-8')
f.writelines(str_out)
f.close()

