from turtle import Turtle

starting_position = (0, -280)
move = 10
finish_line = 280

class Player(Turtle):

    def __init__(self):    
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(move)

    def go_to_start(self):
        self.goto(starting_position)

    def is_at_finish_line(self):
        if self.ycor() > finish_line:
            return True
        else:
            return False
