from data_database import BallsDB
from physic import PhysicsCalculate
from dropper import dropper
from sound_master import sound
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
        self.screen.addshape("image/exit.gif")

        self.screen.title("Funny Merge Balls")
        rootwindow = self.screen.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        rootwindow.resizable(False, False)

        self._game_over = False
        self.__start_val = False

        self.dropper = dropper(self.canvas_height, self.canvas_width)
        self.wall = turtle.Turtle()
        self.title = turtle.Turtle()
        self.logo = turtle.Turtle()
        self.exit_button = turtle.Turtle()
        self.score_text = turtle.Turtle()
        self.Highscore_text = turtle.Turtle()

        self.dropper.hide()
        self.wall.hideturtle()
        self.title.hideturtle()
        self.logo.hideturtle()
        self.exit_button.hideturtle()
        self.score_text.hideturtle()
        self.Highscore_text.hideturtle()

    def __border(self):
        self.wall = turtle.Turtle()

        self.wall.penup()
        self.wall.setheading(0)
        self.wall.pensize(2)
        self.wall.color((255, 0, 0))
        self.wall.goto((-self.canvas_width/2) + 50, (self.canvas_height/2) - 220)
        self.wall.pendown()
        self.wall.forward(self.canvas_width - 100)

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
        self.wall.penup()

        self.wall.hideturtle()
        self.dropper.show()

    def __ui_ingame(self):
        self.exit_button = turtle.Turtle()
        self.exit_button.shape("image/exit.gif")
        self.exit_button.showturtle()
        self.exit_button.penup()
        self.exit_button.goto((self.canvas_width/2) - 50, (-self.canvas_height/2) + 40)

        self.score_text = turtle.Turtle()
        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.goto((-self.canvas_width/2) + 20, (self.canvas_height/2) - 40)
        self.score_text.color("#863f1f")
        self.score_text.write(f"Score: {self._score}", align="left", font=("Comic Sans MS", 20, "bold"))

        self.Highscore_text = turtle.Turtle()
        self.Highscore_text.penup()
        self.Highscore_text.hideturtle()
        self.Highscore_text.goto((-self.canvas_width/2) + 20, (self.canvas_height/2) - 60)
        self.Highscore_text.color("#72381e")
        self.Highscore_text.write(f"Highscore: {self.highscore}", align="left", font=("Comic Sans MS", 10, "bold"))



        self.exit_button.onclick(self.run)

    def __start(self):
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
        sound().gameover.play()
        #TODO: clear scene and appear play again.

    def __space(self):
        if not self.__start_val:
            self.__start_val = True
            self._game_over = False

            turtle.clear()
            self.title.clear()
            self.logo.hideturtle()

            sound().start.play()
            self.__border()
            self.__ui_ingame()
            turtle.update()
        else:
            sound().drop.play()
            print("drop")

    def run(self, _=None, __=None, ___=None):
        #TODO: Runable code.
        turtle.clear()
        self.title.clear()
        self.logo.hideturtle()
        self.exit_button.hideturtle()
        self.wall.clear()
        self.dropper.hide()
        self.score_text.clear()
        self.Highscore_text.clear()
        self.__start()
        turtle.listen()
        turtle.onkey(self.__space, 'space')

        turtle.done()