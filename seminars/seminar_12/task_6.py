class TicTacToeBoard:
    def __init__(self):
        self.array = [['07', '08', '09'],
                      ['04', '05', '06'],
                      ['01', '02', '03']]

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
        elif self.array[1][0] and self.array[1][1] and self.array[1][2] == self.array[1][0]:
            return self.array[1][0]
        elif self.array[2][0] and self.array[2][1] and self.array[2][2] == self.array[2][0]:
            return self.array[2][0]
        elif self.array[0][0] and self.array[1][1] and self.array[2][2] == self.array[0][0]:
            return self.array[0][0]
        elif self.array[2][0] and self.array[1][1] and self.array[0][2] == self.array[2][0]:
            return self.array[2][0]
        elif self.array[0][0] and self.array[1][0] and self.array[2][0] == self.array[0][0]:
            return self.array[0][0]
        elif self.array[0][1] and self.array[1][1] and self.array[2][1] == self.array[0][1]:
            return self.array[0][1]
        elif self.array[0][2] and self.array[1][2] and self.array[2][2] == self.array[0][2]:
            return self.array[0][2]

    def cll(self, i):
        dct = {
            1: self.array[2][0].__add__('x'),
            2: self.array[2][1],
            3: self.array[2][2],
            4: self.array[1][0],
            5: self.array[1][1],
            6: self.array[1][2],
            7: self.array[0][0],
            8: self.array[0][1],
            9: self.array[0][2]
        }

        return dct.values()


def viewX():
    text = int(input('Поставьте крестик на свободном поле: '))
    l = board.cll(text)
    print(*l)

board = TicTacToeBoard()

viewX()
print(*board.get_field(), sep='\n')
