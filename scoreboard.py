from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10, 260)
        self.score = 0
        self.write(arg=f"Score: 0", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 48, "normal"))
