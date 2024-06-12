import keyboard
from time import sleep

def numberHandle(number):
    if number < 10:
        keyboard.send(str(number))
    else:
        number = str(number)
        i = 0
        for letter in number:
            keyboard.send(number[i])
            i += 1

def boardSetup():
    keyboard.send("alt+h")
    keyboard.send("o")
    keyboard.send("d")
    keyboard.send("3")
    keyboard.send("enter")

    for i in range(0, 26):
        keyboard.send("shift+space")
        keyboard.send("alt+h")
        keyboard.send("h")
        keyboard.send("right")
        keyboard.send("enter")
        keyboard.send("down")
    
    keyboard.send("f5")
    keyboard.send("a")
    keyboard.send("a")
    keyboard.send("1")
    keyboard.send("enter")
    keyboard.send("ctrl+space")
    keyboard.send("alt+h")
    keyboard.send("h")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("enter")
    
    keyboard.send("ctrl+left")

    keyboard.send("ctrl+space")
    keyboard.send("alt+h")
    keyboard.send("h")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("enter")

    keyboard.send("left")

    keyboard.send("shift+space")
    keyboard.send("alt+h")
    keyboard.send("h")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("down")
    keyboard.send("enter")


    


class Cursor:
    def __init__(self):
        self.col = 1
        self.row = "a"

    def move(self, col, row):
        self.col = col
        self.row = row
        keyboard.send("f5")
        keyboard.send(col)
        numberHandle(row)
        keyboard.send("enter")

    def place(self):
        keyboard.send("alt+h")
        keyboard.send("h")
        keyboard.send("enter")

    def delete(self):
        keyboard.send("alt+h")
        keyboard.send("h")
        keyboard.send("right")
        keyboard.send("enter")


    #TODO, update row and col position with each move
    def left(self):
        
        keyboard.send("left")

    def right(self):
        keyboard.send("right")

    def up(self):
        keyboard.send("up")

    def down(self):
        keyboard.send("down")    

class Snake:
    def __init__(self):
        self.length = 1
        self.direction = "left"
    
    def create(self, cursor):
        cursor.place()
    
    def move(self, cursor):
        cursor.delete()
        cursor.right()
        cursor.place()
        




    

def main():
    sleep(3)
    #boardSetup()
    cursor = Cursor()
    cursor.move("b", 2)
    snake = Snake()
    snake.create(cursor)

    i = 0
    while i < 10:
        if keyboard.is_pressed("down") == True:
            print("based!!!!")
        snake.move(cursor)
        i += 1


def test():
    while True:
        if keyboard.is_pressed("down") == True:
            print("based!!!!")
            



test()
    
