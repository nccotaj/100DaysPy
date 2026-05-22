from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0 
        self.high_score = self.highscore_read()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.teleport(0,280)
        self.display()


    def display(self):
        self.clear()
        self.write(f"Score: {self.value} High Score: {self.high_score}", False, align="center", font= (16))

    def update(self):
        self.value += 1
        self.display()

    def reset(self):
        if self.value > self.high_score:
            self.high_score = self.value
        
        self.highscore_write()
        self.value = 0
        self.display()

    def highscore_read(self):
        with open("data.txt", mode = "r") as file:  #with keyword closes the file after we are done with it 
            return int(file.read())
    
    def highscore_write(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        
       


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=(16))
        



