"""This module create balls and config everything"""

import turtle

class Balls:
    """
    config balls for physics and gameplay.
    """
    def __init__(self, weigth:int, height:int, preset, database):
        self.weigth = weigth
        self.height = height
        self.property = preset
        self.ball_db = database
        self.random_property = 0

    def generate(self, random_property:int = 0, origin:tuple = (0,0)):
        """
        generate ball for dropper to drop.
        """
        self.random_property = random_property
        self.current_property = self.property[self.random_property]
        self.ball = turtle.Turtle()
        self.ball.penup()
        self.ball.fillcolor(self.current_property["Color"])
        self.ball.color(self.current_property["Color"])
        self.ball.goto(origin)
        self.ball.goto(origin[0]+self.current_property["Radius"], origin[1]+self.current_property["Radius"])
        self.ball.hideturtle()
        self.ball.pendown()
        self.ball.begin_fill()
        self.ball.circle(self.current_property["Radius"])
        self.ball.end_fill()
        self.ball.penup()
        return self.ball, random_property

