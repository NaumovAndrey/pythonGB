class Balance:
    def __init__(self):
        self.arr_right = []
        self.arr_left = []

    def add_right(self, number):
        self.arr_right.append(number)

    def add_left(self, number):
        self.arr_left.append(number)

    def result(self):
        sum_rigth = sum(self.arr_right)
        sum_left = sum(self.arr_left)
        if sum_rigth > sum_left:
            return "r"
        elif sum_rigth < sum_left:
            return "l"
        else:
            "="


balance = Balance()

balance.add_right(10)
balance.add_left(12)
balance.add_right(3)
print(balance.result())
