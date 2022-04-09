from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sc1 = 0
        self.sc2 = 0

    def score_p1(self,s1):
        if self.sc1 < s1 :
             self.clear()
        sc1 = s1
        self.goto(-100, 200)
        self.write(s1, align="center", font=("Arial", 50, "normal"))

    def score_p2(self,s2):
        if self.sc2 < s2 :
             self.clear()
        sc2 = s2
        self.goto(100, 200)
        self.write(s2, align="center", font=("Arial", 50, "normal"))

