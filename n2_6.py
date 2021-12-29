'''* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}), (2, {“название”: “принтер”,
“цена”: 6000, “количество”: 2, “eд”: “шт.”}), (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”:
“шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{“название”: [“компьютер”, “принтер”, “сканер”], “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”:
[“шт.”]'''
ind=1
prod_list=[]
while True:
    try:
        prod_charact = input('Введите через запятую  название, цену, количество товаров и единицу измерения. Для выхода нажмите q : ')
        if prod_charact == 'q': break
        prod_charact=prod_charact .split(',')
        prod_param={'название':prod_charact[0], 'цена':float(prod_charact[1]), 'количество':int(prod_charact[2]), 'единица измерения':prod_charact[3]}
        prod=(ind, prod_param)
        ind+=1
        prod_list.append(prod)
    except:
        print("Данные введены неверно.")
print(prod_list)


keys_prod = list(prod_list[1][1].keys())
list_name=[]
list_price=[]
list_numb=[]
list_unit=[]
dict_statistic={}
#print(keys_prod)
for list_prod in prod_list:
    list_name.append(list_prod[1][keys_prod[0]])
    list_price.append(list_prod[1][keys_prod[1]])
    list_numb.append(list_prod[1][keys_prod[2]])
    list_unit.append(list_prod[1][keys_prod[3]])

dict_statistic[keys_prod[0]]=list_name
dict_statistic[keys_prod[1]]=list_price
dict_statistic[keys_prod[2]]=list_numb
dict_statistic[keys_prod[3]]=list_unit
print(dict_statistic)

