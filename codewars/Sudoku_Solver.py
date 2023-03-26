from typing import List
import string

class Sudoku:
    digits = set([int(el) for el in list(string.digits)[1:]])
    def __init__(self, sudoku:List[List[float]]):
        self.sudoku = sudoku
        self.stack_squares=[]
        self.unfree_fields=set()
        for idx, row in enumerate(self.sudoku):
            for jdx, el in enumerate(row):
                if el!=0:
                    self.unfree_fields.add(idx*9+jdx)
        self.__init_squares()
        self.__insert_value()
    def __init_squares(self):
        square =[]
        for k in range(0, 9, 3):
            for m in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        square.append(self.sudoku[k+i][m+j])
                self.stack_squares.append([k+m//3, Sudoku_square(square)])
                square=[]
    def __insert_value(self):
        while len(self.unfree_fields)<81:
            for i_sq, sq in self.stack_squares:
                sq_row, sq_col = i_sq // 3, i_sq % 3  # number of square 3x3
                free_global_idxs_squares = [[sq_row * 3 + el // 3, el % 3 + sq_col * 3]
                                            for el in sq.free_fields]
                for num in sq.free_digits:
                    free_global_idxs_lines =[]
                    for free in free_global_idxs_squares:
                        if not(self.check_num_in_row(num, free[0]) or
                                   self.check_num_in_column(num, free[1])):
                            free_global_idxs_lines.append(free)

                    if len(free_global_idxs_lines)==1:
                        gl_i = free_global_idxs_lines[0][0]
                        gl_j = free_global_idxs_lines[0][1]
                        self.sudoku[gl_i][gl_j]=num
                        self.unfree_fields.add(gl_i*9+gl_j)
                        sq_i, sq_j = gl_i%3, gl_j%3
                        sq.square[sq_i*3+sq_j]=num
                        self.stack_squares[i_sq][1] =Sudoku_square(sq.square)
    def check_not_null(self):
        for squar in self.stack_squares:
            if 0 in squar:
                return False
        return True
    def check_num_in_row(self, num, idx):
        return num in self.sudoku[idx]
    def check_num_in_column(self, num, jdx):
        col = [el[jdx] for el in self.sudoku]
        return num in col

    def __str__(self):
        self.print_sudoku = []
        for idx, row in enumerate(self.sudoku):
            self.print_sudoku.append(row[:3]+['|']+row[3:6]+['|']+row[6:])
            if idx==2 or idx==5:
                self.print_sudoku.append(['_']*10)
        for row in self.print_sudoku:
            print(*row)
        return 'success!'

class Sudoku_square:
    digits = set([int(el) for el in list(string.digits)[1:]])
    def __init__(self, square:List[float]):
        self.square =square
        self.free_digits = self.digits - {el for el in self.square if el!=0}
        self.free_fields=[idx for idx, el in enumerate(square) if el==0]
    def check_different(self):
        a = [el for el in self.square if el]
        return len(a)==len(set(a))
    def __str__(self):
        return ' '. join([str(el) for el in self.square])
    def check_full(self):
        return (0 not in self.square)


def sudoku(puzzle):
    return Sudoku(puzzle).sudoku


