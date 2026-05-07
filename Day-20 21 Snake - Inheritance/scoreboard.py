from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0 
        self.color("White")
        self.hideturtle()
        self.display()


    def display(self):
        self.penup()
        self.teleport(0,280)
        self.write(f"Score: {self.value}", False, align="center", font= (16))

    def update(self):
        self.value += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=(16))
        



