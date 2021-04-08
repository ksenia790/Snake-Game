from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.tracer(0)

snake = Snake()   # create snakes
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.snake_up, 'w')
screen.onkey(snake.snake_down, 's')
screen.onkey(snake.snake_left, 'a')
screen.onkey(snake.snake_right, 'd')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scores()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
