'''. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
 учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
 Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

def my_parser(sub_str):
    tempo_numb=''
    flag_digit=False
    sum_hour=0
    for ind in sub_str:
        if ind.isdigit():
            tempo_numb+=ind
            flag_digit = True
        elif flag_digit == True:
            flag_digit = False
            sum_hour+=int(tempo_numb)
            tempo_numb = ''
    return sum_hour
if __name__=='__main__':
    file_name='data_for_6.txt'
    out_dict={}
    try:
        f = open(file_name, encoding='utf-8')
        for str_inp in f:
            tempo_l = str_inp.split(':')
            out_dict[tempo_l[0]] = my_parser(tempo_l[1])
    except FileNotFoundError:
        print('Такого файла нет')
    print(out_dict)
