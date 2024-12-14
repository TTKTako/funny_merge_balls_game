import turtle

class dropper:
    def __init__(self, canvas_height, canvas_width):
        turtle.Screen().addshape("image/tube.gif")
        self.paddle = turtle.Turtle()
        self.paddle.penup()
        self.paddle.goto(0, (canvas_height/2) - 140)
        self.paddle.shape("image/tube.gif")
        self.range = [-(canvas_width/2) + 90,(canvas_width/2) + 90]

    def show(self):
        self.paddle.showturtle()

    def hide(self):
        self.paddle.hideturtle()