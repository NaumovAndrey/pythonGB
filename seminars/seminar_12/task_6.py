class TicTacToeBoard:
    def __init__(self):
        self.row = 0
        self.columns = 0
        self.value = 'X'
        self.array = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def new_game(self):
        self.array = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def get_field(self):
        return self.array

    def make_move(self, row, columns):
        if self.array[0][0] and self.array[0][1] and self.array[0][2] == self.array[0][0]:
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

    def inputPosition(self):
        self.row = int(input('Введите номер строки: '))
        while self.row < 1 or self.row > 3:
            self.row = int(input('Введите номер строки: '))

        self.columns = int(input('Введите номер колонки: '))
        while self.columns < 1 or self.columns > 3:
            self.columns = int(input('Введите номер колонки: '))

    def motion(self):
        for i in range(9):
            print('\n'.join(['\t'.join(i) for i in self.array]))
            if i % 2 == 0:
                print('Ходит "X"')
                self.value = 'X'
            else:
                print('Ходит "O"')
                self.value = 'O'
            self.inputPosition()
            if (self.array[self.row - 1][self.columns - 1]) != '-':
                print('Позиция занята')
                self.inputPosition()

            self.array[self.row - 1][self.columns - 1] = self.value

            res = self.make_move(self.row, self.columns)
            if res == "X" or res == 'O':
                print(f'Выйграл <{res}>')
                print()
                self.new_game()
                self.motion()


tic = TicTacToeBoard()
tic.motion()

# board = TicTacToeBoard()
# print(*board.get_field(), sep='\n')
