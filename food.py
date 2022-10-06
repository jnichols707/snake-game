from turtle import Turtle
import random 

class Food(Turtle):
    def __init__(self):
        super().__init__() #inherits from Turtle
        self.shape("circle")
        self.color("orange")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        rand_x = random.randint(-380,380)
        rand_y = random.randint(-380,380)
        self.goto(rand_x,rand_y)

    def get_eaten(self):
        new_x = random.randint(-380,380)
        new_y = random.randint(-380,380)
        self.goto(new_x, new_y)

