from turtle import Turtle


ORIGIN = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self): #updates the ymove attribute which affects the move method
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(ORIGIN)
        self.move_speed = 0.1
        self.bounce_x()
        