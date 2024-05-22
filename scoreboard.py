from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.chances = 3
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-390, 260)
        self.write(f"Score:{self.score} Chances:{self.chances}", font=FONT)

    def point(self):
        self.clear()
        self.score += 10
        self.write(f"Score:{self.score} Chances:{self.chances}", font=FONT)

    def take_chance(self):
        self.clear()
        self.chances -= 1
        self.write(f"Score:{self.score} Chances:{self.chances}", font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("You win", align='center', font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=FONT)
