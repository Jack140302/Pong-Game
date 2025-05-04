from turtle import Turtle


class paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.speed('fast')
        self.penup()
        self.goto(position)

    # def side(self, side='left'):  #without using position function
    #     if side == 'left':
    #         self.goto(-350, 0)
    #     else:
    #         self.goto(350, 0)

    def move_paddle_up(self):
        self.goto(self.xcor(), 20 + self.ycor())

    def move_paddle_down(self):
        self.goto(self.xcor(), -20 + self.ycor())
