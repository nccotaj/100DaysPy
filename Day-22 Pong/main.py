from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


#screen setup
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")

#turn off animation untill update is called
screen.tracer(0)


right_paddle = Paddle(350)
left_paddle = Paddle(-350)

ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")



game_is_on = True


#game update needs to be in while loop to allow for the movement, other wise it only checks the one time and you won't see any movement
while game_is_on == True:
    time.sleep(ball.move_speed)
    screen.update()


    ball.move()

    #Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect  paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    

    #right paddle miss:
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score += 1
        score.update()

    #left paddle miss:
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score += 1
        score.update()








screen.exitonclick()