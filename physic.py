"""This module calculate the physics"""

import turtle
import math
import random
from sound_master import Sound

class PhysicsCalculate:
    """
    for calculate balls physics in x axis and y axis and check is it merge.
    """
    def __init__(self, balldb: list, property_list:list, ball_module, score):
        self.database = balldb
        self.property = property_list
        self.ball_module = ball_module
        self.score = score
        self.drop()

    def draw(self, me, x = 0, y = 0):
        """
        This function draw a movement of balls.
        """
        me[0].clear()
        me[0].goto(me[0].xcor() + x, me[0].ycor() + y)
        me[0].hideturtle()
        me[0].pendown()
        me[0].begin_fill()
        me[0].circle(self.property[me[1]]["Radius"])
        me[0].end_fill()
        me[0].penup()

    def drop(self):
        """
        This function give a gravity into balls.
        """
        for i in self.database:
            if self.check_collision(i):
                continue
            self.draw(i, x = 0, y = -1)

        turtle.Screen().ontimer(self.drop, 1)

    def left_right(self, me, datx):
        """
        This function make balls moveable to left or right.
        """
        push = math.ceil(self.property[me[1]]["Radius"]*0.95)
        hitbox = me[0].xcor() + 2*self.property[me[1]]["Radius"]
        if me[0].xcor() <= -210 or hitbox >= 210:
            if me[0].xcor() < -211:
                self.draw(me, x = push, y = 5)
            elif hitbox >= 211:
                self.draw(me, x = -push, y = 5)
            else:
                return None
        if abs(datx) == 0:
            side = random.randint(0,1)
            if bool(side):
                self.draw(me, x = 1, y = 1)
            else:
                self.draw(me, x = -1, y = 1)
        elif datx > 0:
            self.draw(me, x = -1, y = 1)
        elif datx < 0:
            self.draw(me, x = 1, y = 1)

    def check_collision(self, me):
        """This function check collision."""
        if me[0].ycor() <= -270:
            return True
        for i in self.database:
            if i is me:
                continue
            datx = (i[0].xcor() + self.property[i[1]]["Radius"]) - \
                (me[0].xcor()  + self.property[me[1]]["Radius"])
            daty = (i[0].ycor() + self.property[i[1]]["Radius"]) - \
                (me[0].ycor()  + self.property[me[1]]["Radius"])
            distance = math.sqrt(datx**2 + daty**2)
            if distance <= self.property[me[1]]["Radius"] + self.property[i[1]]["Radius"]:
                self.left_right(me, datx)
                if me[1] == i[1]:
                    self.merge(me, i)
                return True

    def merge(self, m1, m2):
        """This function merge ball to a new one."""
        difference_radius = self.property[(m1[1] + 1) % 12]["Radius"] - \
            self.property[(m1[1]) % 12]["Radius"]
        m1[0].clear()
        m2[0].clear()
        self.database.remove(m1)
        self.database.remove(m2)
        self.score.add_score(self.property[(m1[1] + 1) % 12]["Reward"])
        new_ball, state = self.ball_module.generate(random_property=(m1[1] + 1) % 12, \
                                                    origin=(m1[0].xcor() - difference_radius, m1[0].ycor() + difference_radius + 2))
        self.database.append([new_ball, state, False])
        Sound().merge.play()
