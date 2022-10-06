from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_SPEED = 15

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(position)
            self.snake.append(snake_segment)

    def move(self):
        for i in range(len(self.snake)-1, 0, -1): #range(start, stop, step)
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def eat_food(self):
        x_position = self.snake[-1].xcor()
        y_position = self.snake[-1].ycor()
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(x_position, y_position)
        self.snake.append(snake_segment)
