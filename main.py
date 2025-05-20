from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake() # crete snake from snake class
food = Food()   #create food from food class
scoreboard = Scoreboard() #create scoreboard

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:  #food eating
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # coalition border from -270 to 270 in x and y
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_one = False
        scoreboard.game_over()

    # colliding white own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_one = False
            scoreboard.game_over()


screen.exitonclick() # last line all time ++++++++++++++++++++++++++++++
