import turtle
import math

class PhysicsCalculate:
    def __init__(self, balldb: list, property:list):
        self.database = balldb
        self.property = property
        self.drop()

    def drop(self):
        for i in self.database:
            if self.check_collision(i):
                continue
            i[0].clear()
            i[0].goto(i[0].xcor(), i[0].ycor() - 1)
            i[0].hideturtle()
            i[0].pendown()
            i[0].begin_fill()
            i[0].circle(self.property[i[1]]["Radius"])
            i[0].end_fill()
            i[0].penup()

        turtle.Screen().ontimer(self.drop, 2)

    def check_collision(self, me):
        if me[0].ycor() <= -270:
            return True
        for i in self.database:
            if i is me:
                continue
            datx = (i[0].xcor() + self.property[i[1]]["Radius"]) - (me[0].xcor()  + self.property[me[1]]["Radius"])
            daty = (i[0].ycor() + self.property[i[1]]["Radius"]) - (me[0].ycor()  + self.property[me[1]]["Radius"])
            distance = math.sqrt(datx**2 + daty**2)
            if distance <= self.property[me[1]]["Radius"] + self.property[i[1]]["Radius"]:
                return True