from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 265)
        self.write("Player Left", align='center', font=('Courier', 18, 'normal'))
        self.goto(110, 265)
        self.write("Player Right", align='center', font=('Courier', 18, 'normal'))
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 60, 'normal'))
        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 60, 'normal'))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def left_winner(self):
        self.clear()
        self.color('green')
        self.goto(-100, 265)
        self.write("Player Left", align='center', font=('Courier', 18, 'normal'))
        self.color('red')
        self.goto(110, 265)
        self.write("Player Right", align='center', font=('Courier', 18, 'normal'))
        self.color('white')
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 60, 'normal'))
        self.color('white')
        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 60, 'normal'))

    def right_winner(self):
        self.clear()
        self.color('red')
        self.goto(-100, 265)
        self.write("Player Left", align='center', font=('Courier', 18, 'normal'))
        self.color('green')
        self.goto(110, 265)
        self.write("Player Right", align='center', font=('Courier', 18, 'normal'))
        self.color('white')
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 60, 'normal'))
        self.color('white')
        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 60, 'normal'))