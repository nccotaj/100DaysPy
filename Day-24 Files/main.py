from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

#screensetup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")

#turns off the animiation so that you have to use screen.update()
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


#listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#we turned off the animation but updated the screen with the new state
screen.update()


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    
    snake.move()


    #detect collisoin with food (using distance method which compares distance between turtles)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()
    
    #Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    
    #Detect tail collions
    #Checks Heaad distance from other segments. Ignores the head segment becasue head will always be close to itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: 
            score.reset()
            snake.reset()
    
    
   
   

    
   
        





















screen.exitonclick()