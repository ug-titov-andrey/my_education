'''Реализовать скрипт, в котором должна быть предусмотрена функция
 расчёта заработной платы сотрудника. Используйте в нём формулу:
 (выработка в часах*ставка в час) + премия.
 Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.'''


'''
название ключей параметров -name, prod, bet,prize
ключ предваряется -. То есть параметр с ключом в аргументах передается в виде '-ключ значение' n4_1.py -name petr -bet 10 ... 
'''
import sys
def getopts(argv):
    opts={}
    while argv:
        if argv[0][0]=='-':
            opts[argv[0][1:]]=argv[1]
            argv=argv[2:]
        else:
            argv = argv[1:]
    return opts

def calc_wages(prod, bet,prize):
    return float(prod)*float(bet) +float(prize)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    argv=sys.argv
    data= getopts(argv)
    try:
        wages = calc_wages(data['prod'],data['bet'], data['prize'])
        print('Заработная плата сотрудника %s равняется %g' % (data['name'], wages))
    except (KeyError, ValueError):
        print('Задайте правильные входные данные')
