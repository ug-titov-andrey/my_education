from my_exc import My_exception
class Office_equip:

    def __init__(self, Name,Manufacturer, Color,Format,Permission):
        self._name=Name
        self._manufacturer = Manufacturer
        self._color = Color
        self._format=Format
        self._permission = Permission

    def __str__(self):
        return f'Наименование товара => {self._name}, фирма производитель => {self._manufacturer}, цвет => {self._color}, Формат бумаги => {self._format}, разрешение =>{self._permission}'



class Printer(Office_equip):
    def __init__(self,Manufacturer, Color,Format,Permission,Print_type,Printing,Print_speed):
        Office_equip.__init__(self,'принтер',Manufacturer, Color,Format,Permission)
        self.print_type=Print_type
        self.printing=Printing
        self.print_speed=Print_speed
    def __str__(self):
        return Office_equip.__str__(self) + f', тип принтера => {self.print_type}, печать => {self.printing}, скорость печати => {self.print_speed}'


class Scanner(Office_equip):
    def __init__(self,Manufacturer, Color,Format,Permission,Scan_speed):
        Office_equip.__init__(self,'сканер',Manufacturer, Color,Format,Permission)
        self.scan_speed=Scan_speed
    def __str__(self):
        return Office_equip.__str__(self) + f',   скорость сканирования => {self.scan_speed}'

class Xerox(Office_equip):
    def __init__(self,Manufacturer, Color,Format,Permission,Printing,Scan_speed):
        Office_equip.__init__(self,'ксерокс', Manufacturer, Color,Format,Permission)
        self.scan_speed=Scan_speed
        self.printing = Printing
    def __str__(self):
        return Office_equip.__str__(self) + f',  печать => {self.printing}, скорость сканирования => {self.scan_speed}'

class Warehouse:
    order=[]
    def __init__(self,name_warehouse):
        self.name_warehouse = name_warehouse
        self.numb_product={'принтер':0, 'сканер':0,'ксерокс':0}
        self.list_products=[]
    def put_products(self,Product,number):
        try:
            number = int(number)
        except ValueError:
            raise My_exception(f'Количесто {Product._name}ов должно быть числом')
        while number:
            name = Product._name
            self.list_products.append(Product)
            self.numb_product[name] += 1
            number-=1
    def get_products(self, name_pr, number):
        out_list=[]
        try:
            number = int(number)
        except ValueError:
            raise My_exception(f'Количест {name_pr} должно быть числом')
        report=''
        while number:
            for ind,prod_from_list in enumerate(self.list_products):
                if prod_from_list._name == name_pr.lower():
                    report+=f'{self.list_products[ind]._name} {self.list_products[ind]._manufacturer}  {self.list_products[ind]._color}  выдан со склада \n'
                    out_list.append(self.list_products[ind])
                    del (self.list_products[ind])
                    self.numb_product[name_pr] -= 1
                    number-=1
                    break
            else:
                report+=f'{name_pr}ов больше нет на складе '
                number = 0
        print(report)
        return out_list

if __name__=='__main__':
    printer=['HP','black', 'A4', '1240x1064', 'laser', 'color', 50]

    scaner= ['HP', 'black', 'A4', '1240x1064',  50]
    xerox=['HP','black', 'A4', '1240x1064',  'color',30]
    my_warehouse= Warehouse('Склад офисной  техники')
    try:
        my_warehouse.put_products(Printer('HP','black', 'A4', '1280x10244', 'laser', 'black-white', 50),'5')
        my_warehouse.put_products(Xerox('HP', 'black', 'A4', '1240x1064',  'color', 50), 3)
        my_warehouse.put_products(Scanner('HP', 'black', 'A4', '1240x1064', 50), 9)
        my_warehouse.put_products(Printer('canon', 'white', 'A4', '1240x1064', 'inkjet', 'color', 50), 9)
        office_equip_out1 = my_warehouse.get_products('принтер','7')
        office_equip_out2 = my_warehouse.get_products('сканер', 10)
        print('Со склада выданы\n')
        for office_equip in office_equip_out1:
            print(office_equip)
        print('Со склада выданы')
        for office_equip in office_equip_out2:
            print(office_equip)
    except My_exception as e:
        print(e)














