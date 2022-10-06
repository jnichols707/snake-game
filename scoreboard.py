from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.hideturtle()
        self.score = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,375)
        self.pendown()
        self.write_score()
        # f"Score: {score}",align="center", font=("Arial", 8, "normal")

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier",20,"normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.color("red")
        self.write(f"Game Over! Your score was: {self.score}", align="center", font=("Courier",20,"normal"))

