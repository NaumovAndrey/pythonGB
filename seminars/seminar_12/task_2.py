class Button:
    def __init__(self) -> None:
        self.count=0
    def click(self):
        self.count+=1
    def reset(self):
        self.count=0
    def click_count(self):
        return self.count

button= Button()
button.click()
button.click()
print(button.click_count())
button.reset()
print(button.click_count())
