from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.shapesize(4.5, 1)
        self.color("white")
        self.penup()
        self.goto(pos)

    def up(self):
        self.newy = self.ycor() + 20
        self.goto(self.xcor(), self.newy)

    def down(self):
        self.newy = self.ycor() - 20
        self.goto(self.xcor(), self.newy)
