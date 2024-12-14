from data_database import BallsDB
from physic import PhysicsCalculate
from playsound import playsound
import turtle
import random

class SetUp(BallsDB):
    def __init__(self, username:str="Guest") -> None:
        super().__init__(username)
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = 520
        self.canvas_height = 700
        turtle.setup(self.canvas_width, self.canvas_height)

        self.screen = turtle.Screen()

        self.screen.addshape("image/logo.gif")

        self.screen.title("Funny Merge Balls")
        rootwindow = self.screen.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        rootwindow.resizable(False, False)

        self._game_over = False
        self.__start_val = False

    def __border(self):
        self.wall = turtle.Turtle()
        self.wall.penup()
        self.wall.goto((-self.canvas_width/2) + 50, (self.canvas_height/2) - 170)
        self.wall.pensize(10)
        self.wall.pendown()
        self.wall.color((0, 0, 0))
        self.wall.right(90)
        self.wall.forward(self.canvas_height*0.65)
        self.wall.left(90)
        self.wall.forward(self.canvas_width - 100)
        self.wall.left(90)
        self.wall.forward(self.canvas_height*0.65)

    def __ui_ingame(self):
        pass

    def __start(self):
        print("Start!!!")

        if not self._game_over:
            self.logo = turtle.Turtle()
            self.logo.shape("image/logo.gif")
            self.logo.penup()
            self.logo.goto(0,20)
            self.logo.showturtle()

            self.title = turtle.Turtle()
            self.title.hideturtle()
            self.title.penup()
            self.title.goto(0, (self.canvas_height/2) - 120)
            self.title.color("#3b58fb")
            self.title.write("Funny Merge Balls", align="center", font=("Comic Sans MS", 35, "bold"))
            self.title.goto(0, (-self.canvas_height/2) + 120)
            self.title.color("#fbaa3b")
            self.title.write("Press 'space' to start!", align="center", font=("Comic Sans MS", 14, "bold"))

        self._score = 0
        self._game_over = False
        self.__start_val = False
        turtle.update()

    def __game_over(self):
        self._game_over = True
        self.__start_val = False
        self.save_data()
        playsound('gameover.wav', block=False)
        #TODO: clear scene and appear play again.

    def __space(self):
        if not self.__start_val:
            self.__start_val = True
            self._game_over = False

            turtle.clear()
            self.title.clear()
            self.logo.hideturtle()

            playsound('start.wav', block=False)
            self.__border()
            self.__ui_ingame()
            turtle.update()
        else:
            print("drop")

    def run(self):
        #TODO: Runable code.
        turtle.clear()
        self.__start()
        turtle.listen()
        turtle.onkey(self.__space, 'space')

        turtle.done()
        print("Close")