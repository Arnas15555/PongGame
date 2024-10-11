from turtle import Turtle

LEFT = (-340, 0)
RIGHT = (340, 0)


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create_paddle(self, pos):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
