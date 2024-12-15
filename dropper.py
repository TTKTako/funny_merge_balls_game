"""This module do about dropper."""

import turtle

class Dropper:
    """
    This class create dropper to drop ball.
    """
    def __init__(self, canvas_height, canvas_width):
        self._height = canvas_height
        self._width = canvas_width
        self.screen = turtle.Screen()
        self.screen.addshape("image/tube.gif")

        self.dropper = turtle.Turtle()
        self.dropper.penup()
        self.dropper.goto(-(self._width/2) + 90, (self._height/2) - 140)
        self.dropper.shape("image/tube.gif")
        self.__range = [-(self._width/2) + 90, (self._width/2) - 90]
        self.__where_to_go = 0

    def show(self):
        """
        show dropper.
        """
        self.dropper.showturtle()

    def hide(self):
        """
        hide dropper.
        """
        self.dropper.hideturtle()

    def left_right(self):
        """
        repeatly move dropper left-to-right.
        """
        if self.dropper.xcor() == self.__range[0]:
            self.__where_to_go = 1
        elif self.dropper.xcor() == self.__range[1]:
            self.__where_to_go = -1

        self.dropper.goto(self.dropper.xcor() + self.__where_to_go, self.dropper.ycor())
        turtle.update()
        if self.dropper.isvisible():
            self.screen.ontimer(self.left_right, 10)

    @property
    def posx(self) -> float:
        """
        return X position value of dropper.
        """
        return self.dropper.xcor()

    @property
    def posy(self) -> float:
        """
        return X position value of dropper.
        """
        return self.dropper.ycor()
