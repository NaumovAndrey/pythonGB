class OddEvenSeparator:
    def __init__(self):
        self.li_even = list()
        self.li_odd = list()

    def add(self, number):
        if number % 2:
            self.li_even.append(number)
        else:
            self.li_odd.append(number)

    def result(self):
        return self.li_odd, self.li_even

odd = OddEvenSeparator()

odd.add(10)
odd.add(1)
odd.add(0)
odd.add(6)
odd.add(7)
odd.add(13)
odd.add(9)
odd.add(5)

print(odd.result())



