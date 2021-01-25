# Define cell class
class Cell:
    def __init__(self,row,col,value):
        self.row = row
        self.col = col
        if value in ['1','2','3','4','5','6','7','8','9']:
            self.possible_values = value
        else:
            self.possible_values = ['1','2','3','4','5','6','7','8','9']
    # currently unused
    def get_pos(self):
        return (row,col)
    def block_finder(self,n):
        if n < 3:
            return 0
        elif n < 6:
            return 1
        else:
            return 2
    def get_block(self):
        return (self.block_finder(self.row),self.block_finder(self.col))
    def get_value(self):
        if len(self.possible_values) == 1:
            return self.possible_values[0]
        else:
            return '*'
    def set_value(self,n):
        self.possible_values = [n]
    def remove_value(self,n):
        if n in self.possible_values:
            self.possible_values.remove(n)

# Define sudoku class
class Sudoku:
    def __init__(self,values):
        self.cells = list()
        for r in range(9):
            self.cells.append(list())
            for c in range(9):
                self.cells[r].append(Cell(r,c,values[r][c]))
    def print_sudoku(s):
        for r in range(9):
            if r % 3 == 0:
                print('-'*((9+4)*2-1))
            p = ''
            for c in range(9):
                if c % 3 == 0:
                    p += '| '
                p += s.get_cell_value(r,c) + ' '
            p += '|'
            print(p)
        print('-'*((9+4)*2-1))
    def get_possible_values(self,r,c):
        return self.cells[r][c].possible_values
    def remove_possible_value(self,r,c,v):
        self.cells[r][c].remove_value(v)
    def get_cell_value(self,r,c):
        return self.cells[r][c].get_value()
    def is_solved(self):
        for r in range(9):
            for c in range(9):
                if self.get_cell_value(r,c) == '*':
                    return False
        return True
    def reduce_cell(self,r,c):
        for s in range(9):
            if r != s:
                # remove from (r,c) the value of (s,c)
                self.remove_possible_value(r,c,self.get_cell_value(s,c))
        for d in range(9):
            if c != d:
                # remove from (r,c) the value of (r,d)
                self.remove_possible_value(r,c,self.get_cell_value(r,d))
        block = self.cells[r][c].get_block()
        for s in range(9):
            for d in range(9):
                # if not in same row or column but in same block
                if r!=s and c!=d and self.cells[s][d].get_block() == block:
                    # remove from (r,c) the value of (s,d)
                    self.remove_possible_value(r,c,self.get_cell_value(s,d))

class Sequence:
    # TODO: create row and column (and block?) class

# enter starting values
# NYT easy 6/4/2020
# input = [   ['8','*','1','9','3','*','*','4','2'],
#             ['*','*','5','*','*','2','3','*','8'],
#             ['3','*','4','5','1','*','*','*','*'],
#             ['*','8','*','*','*','9','*','5','4'],
#             ['2','9','*','4','*','1','*','7','*'],
#             ['5','4','*','*','*','7','9','6','*'],
#             ['7','3','*','*','8','*','*','*','*'],
#             ['*','*','*','2','9','5','4','*','*'],
#             ['*','*','*','1','*','*','6','*','9']]

# NYT medium 6/4/2020
# input = [   ['1','*','5','6','*','*','*','*','*'],
#             ['*','6','3','9','*','4','*','*','*'],
#             ['*','*','*','*','*','*','*','*','*'],
#             ['*','*','6','*','*','8','1','5','*'],
#             ['2','*','*','*','*','*','*','9','7'],
#             ['*','*','*','*','*','1','8','*','*'],
#             ['*','5','2','*','6','*','3','*','*'],
#             ['*','*','9','1','*','*','*','*','8'],
#             ['*','7','*','*','*','3','*','*','5']]

# NYT easy 6/5/2020
input = [   ['*','3','*','1','6','*','*','*','4'],
            ['*','2','*','4','*','7','9','*','3'],
            ['7','*','*','*','*','9','*','1','2'],
            ['*','*','*','3','*','*','1','2','*'],
            ['1','4','8','*','*','*','7','*','*'],
            ['*','*','*','7','1','6','4','9','*'],
            ['8','*','6','*','5','*','*','*','*'],
            ['*','7','5','*','9','*','2','6','*'],
            ['*','*','2','6','*','4','*','8','9']]
# initiate sudoku
sudoku = Sudoku(input)


print('start')
sudoku.print_sudoku()

i = 1
while (sudoku.is_solved() == False):
    for r in range(9):
        for s in range(9):
            sudoku.reduce_cell(r,s)
    print('Round {}'.format(i))
    sudoku.print_sudoku()
    i+=1
    if i > 5:
        break
