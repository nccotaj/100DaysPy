import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


tim = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()

screen.onkey(tim.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    #everygame tick create a new car
    car_manager.create_car()

    #everygame tick move the cars
    car_manager.move_cars()

    #detect collision
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            score.game_over()
            game_is_on = False


    #Detect Level Completion (succesful crossing)
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        score.score_increase()
        
    





screen.exitonclick()
