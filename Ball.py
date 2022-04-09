from turtle import Turtle

class Ball(Turtle):

    is_upward = True
    score_p2 = 0
    score_p1 = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.x=10
        self.y=10

    def move(self):
        newy = self.ycor() + self.y
        newx = self.xcor() + self.x
        self.goto(newx,newy)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset(self):
        self.goto(0,0)






