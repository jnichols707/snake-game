from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)


jake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(jake.go_up,"Up") #don't include parentheses in function call from another class or else it will triger automatically w/o keypress
screen.onkey(jake.go_left,"Left")
screen.onkey(jake.go_right, "Right")
screen.onkey(jake.go_down, "Down")


game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.05)
    jake.move() 
    if jake.head.distance(food) < 15:
        jake.eat_food()
        food.get_eaten()
        scoreboard.update_scoreboard()

    if jake.head.xcor() >= 390 or jake.head.xcor() <= -390 or jake.head.ycor() >= 390 or jake.head.ycor() <= -390:
        game_over = True
        scoreboard.game_over()
    
   

    for segment in jake.snake[1::]:
        if jake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()
    

screen.exitonclick()