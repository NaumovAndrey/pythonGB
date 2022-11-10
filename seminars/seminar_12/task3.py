class BigBell:
    def __init__(self) -> None:
        self.x = True

    def sound(self):
        if self.x == True:
            print("ding")
            self.x = False
        else:
            print("dong")
            self.x = True


bell = BigBell()
while True:
    bell.sound()
