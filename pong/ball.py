from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        # self.direction = "up"
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # MY OG SOLUTION

        # if self.ycor() > 280:
        #     self.direction = "down"
        # elif self.ycor() < -280:
        #     self.direction = "up"
        #
        # if self.direction == "down":
        #     new_y = self.ycor() - 10
        # elif self.direction == "up":
        #     new_y = self.ycor() + 10

        self.goto(new_x, new_y)

        # way better solution
    def bounce(self):
        self.y_move *= -1

    def change_direction(self):
        self.x_move *= -1
