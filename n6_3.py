'''3. Реализовать базовый класс Worker (работник).
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника
    (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position,
    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker:
    def __init__(self, Name,Surname, Position, Wage, Bonus):
        self.name=Name
        self.surname=Surname
        self.position=Position
        self._income=dict(wage=float(Wage), bonus=float(Bonus))

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_attr_value(self):
        return f'Имя - {self.name} \nфамилия - {self.surname}  \nДолжность - {self.position}\nОклад - {self._income["wage"]}\nПремия - {self._income["bonus"] *100}%\n_____'

    def get_total_income(self):
        return self._income['wage'] +self._income['wage']*self._income['bonus']



if __name__=='__main__':
    worker = Worker("Иван", "Иванов", "Сварщик", 57000, 0.3)
    print(worker.get_attr_value())
    print(f'суммарный доход сотрудника {worker.get_full_name()} равен {worker.get_total_income()}')
