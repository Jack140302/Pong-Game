from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pensize(5)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pendown()
        self.forward(600)
