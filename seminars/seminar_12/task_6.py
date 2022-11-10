class TicTacToeBoard:
    def __init__(self):
        self.array = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def new_game(self):
        self.array = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def get_field(self):
        return self.array


    def make_move(self, row, column):
        if self.array[row][column] == 'x' or self.array[row][column] == '0':
            print('Эта ячейка занята')
        elif self.array[0][0] and self.array[0][1] and self.array[0][2] == self.array[0][0]:
            return self.array[0][0]
        elif self.array[][] and self.array[][] and self.array[][] == self.array[0][0]:
            return self.array[0][0]


board = TicTacToeBoard()

print(*board.get_field(), sep='\n')
