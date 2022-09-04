'''Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.'''
file_name='data_for_2.txt'
templ_list=['-', '?', '!', ',',';', '']
out_list =[]
try:
    f= open(file_name, 'r', encoding='utf-8')
    for ind,f_str in enumerate(f):
        numb_word=0
        list_word=f_str.split()
        list_word_f=[w for w in list_word if w not in templ_list]
        out_list.append(f'В {ind+1} строке {len(list_word_f)} слов')
    else:
        print(f'В файле {file_name}  {ind+1} строк. \n _______________________')
        print('\n'.join(out_list))
except IOError:
    print('Ошибка чтения файла')
finally:
    f.close()
