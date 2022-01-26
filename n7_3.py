''' '''
class My_exception(Exception):
    def __init__(self, report):
        self.report = report
    def __str__(self):
        return self.report
class Cell:
    def __init__(self, numb_cells):
        self.numb_cells=numb_cells
    def __add__(self, other):
        return Cell(self.numb_cells + other.numb_cells)
    def __sub__(self, other):
        if self.numb_cells <= other.numb_cells:
            raise My_exception('Ошибка при вычитании. Число ячеек во второй клетке должно быть меньше числа ячеек в первой клетке')
        else:
            return  Cell(self.numb_cells - other.numb_cells)

    def __mul__(self, other):
        return Cell(self.numb_cells * other.numb_cells)

    def __truediv__(self, other):
        return Cell(self.numb_cells // other.numb_cells)
    def make_order(self, ncols):
        out_str=''
        nrows= self.numb_cells//ncols
        remains= self.numb_cells%ncols
        for i in range(nrows):
            out_str+='*'* ncols + '\n'
        out_str+='*'* remains
        return out_str


if __name__=='__main__':
    A=Cell(23)
    B=Cell(24)
    try:
        C= A-B
        print(C.make_order(15))
    except My_exception as e:
        print(e)



