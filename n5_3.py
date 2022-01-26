'''3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
 Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
 Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''
file_name='data_for_3.txt'
salary=0
list_employee=[]
try:
    f= open(file_name, 'r', encoding='utf-8')
    ind = 0
    for f_str in f:

        tempo = f_str.split()
        #print(f_str+'______________')
        if len(tempo)==2:
            try:
                employee_t, salary_t = tempo[0], float(tempo[1])
                if salary_t < 20000:
                    list_employee.append(employee_t)
                ind+=1
                salary += salary_t
            except ValueError:
                print(f'Для сотрудник {employee_t} зарплата введена в неправильом формате')
except IOError:
    print('Ошибка чтения файла')
else:
    print('Список сотрудников с зарплатами ниже 20000р: \n' + '\n'.join(list_employee))
    print('____________________________')
    print(f'Средняя зарплата сотрудников => {salary/(ind)}')
finally:
    f.close()