'''. Создать вручную и заполнить несколькими строками текстовый файл,
 в котором каждая строка будет содержать данные о фирме:
  название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json
file_name='data_for_7.txt'
file_name_json='user_data7.json'
firmdict={}
profit_sum=0
ind=0
report=''
with open(file_name) as f:
    for data_str in f:
        firm_tempo= data_str.split()
        try:
            profit = float(firm_tempo[2])-float(firm_tempo[3])
            if profit >= 0:
                profit_sum+=profit
                ind+=1
            firmdict[firm_tempo[0]] = profit
        except (TypeError, ValueError):
            report += f'Данные фирмы {firm_tempo[0]} заполнены неверно \n'
        else:
            average_profit=profit_sum/ind
with open(file_name_json,'w') as f:
    json.dump([firmdict, {'average_profit':average_profit}], f)
print(report)




