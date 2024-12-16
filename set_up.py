from data_database import BallsDB
from run_balls import Balls
from dropper import Dropper
from physic import PhysicsCalculate
from sound_master import Sound
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
        self.screen.bgpic("image/bg.gif")
        rootwindow = self.screen.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        rootwindow.resizable(False, False)

        self._game_over = False
        self.__start_val = False

        self.random_num = random.randint(0,4)
        self.dropper = Dropper(self.canvas_height, self.canvas_width)
        self.ball_module = Balls(self.canvas_width, self.canvas_height, self.property, self.ball_db)
        self.physic = PhysicsCalculate(self.ball_db, self.property, self.ball_module, super())
        self.wall = turtle.Turtle()
        self.title = turtle.Turtle()
        self.logo = turtle.Turtle()
        self.exit_button = turtle.Turtle()
        self.score_text = turtle.Turtle()
        self.Highscore_text = turtle.Turtle()
        self.guild = turtle.Turtle()
        self.over_text = turtle.Turtle()
        self.over_text_left = turtle.Turtle()
        self.over_text_right = turtle.Turtle()
        self.over_text_restart = turtle.Turtle()
        self.show_ball = turtle.Turtle()

        self.dropper.hide()
        self.wall.hideturtle()
        self.title.hideturtle()
        self.logo.hideturtle()
        self.exit_button.hideturtle()
        self.score_text.hideturtle()
        self.Highscore_text.hideturtle()
        self.guild.hideturtle()
        self.over_text.hideturtle()
        self.over_text_left.hideturtle()
        self.over_text_right.hideturtle()
        self.over_text_restart.hideturtle()
        self.show_ball.clear()
        self.show_ball.hideturtle()

    def __border(self):
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

    def __update_score(self):
        self.score_text.reset()
        if not self._game_over and self.__start_val:
            self.score_text.clear()
            self.score_text.penup()
            self.score_text.hideturtle()
            self.score_text.goto((-self.canvas_width/2) + 20, (self.canvas_height/2) - 40)
            self.score_text.color("#fffbb5")
            self.score_text.write(f"Score: {self.score}", align="left", font=("Comic Sans MS", 20, "bold"))
            self.screen.ontimer(self.__update_score, 10)
        else:
            self.score_text.clear()

    def __ui_ingame(self):
        self.next_ball(self.property[self.random_num])
        self.exit_button.shape("image/exit.gif")
        self.exit_button.showturtle()
        self.exit_button.penup()
        self.exit_button.goto((self.canvas_width/2) - 50, (-self.canvas_height/2) + 40)

        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.goto((-self.canvas_width/2) + 20, (self.canvas_height/2) - 40)
        self.score_text.color("#fffbb5")
        self.score_text.write(f"Score: {self.score}", align="left", font=("Comic Sans MS", 20, "bold"))

        self.Highscore_text.penup()
        self.Highscore_text.hideturtle()
        self.Highscore_text.goto((-self.canvas_width/2) + 20, (self.canvas_height/2) - 70)
        self.Highscore_text.color("#ffffff")
        self.Highscore_text.write(f"Highscore: {self.highscore}", align="left", font=("Comic Sans MS", 15, "bold"))
        self.Highscore_text.goto((-self.canvas_width/2) + 20, -(self.canvas_height/2) + 20)
        self.Highscore_text.write(f"Player: {self.username}", align="left", font=("Comic Sans MS", 15, "bold"))
        self.Highscore_text.goto((self.canvas_width/2) - 110, (self.canvas_height/2) - 30)
        self.Highscore_text.write(f"Next ball: ", align="left", font=("Comic Sans MS", 15, "bold"))

        self.guild.penup()
        self.guild.goto(0, -130)
        self.guild.color("#000000")
        self.guild.write("Press 'space' to drop ball!", align="center", font=("Comic Sans MS", 14, "bold"))

        self.exit_button.onclick(self.run)
        self.dropper.left_right()

    def next_ball(self, info):
        self.show_ball.penup()
        self.show_ball.clear()
        self.show_ball.goto((self.canvas_width/2) - 35, (self.canvas_height/2) - 60)
        self.show_ball.hideturtle()
        self.show_ball.pendown()
        self.show_ball.color(info["Color"])
        self.show_ball.fillcolor(info["Color"])
        self.show_ball.begin_fill()
        self.show_ball.circle(12)
        self.show_ball.end_fill()
        self.show_ball.penup()

    def __start(self):
        self.__clear()
        if not self._game_over:
            self.score_text.clear()
            self.logo.shape("image/logo.gif")
            self.logo.penup()
            self.logo.goto(0,20)
            self.logo.showturtle()

            self.title = turtle.Turtle()
            self.title.hideturtle()
            self.title.penup()
            self.title.goto(0, (self.canvas_height/2) - 120)
            self.title.color("#ffffff")
            self.title.write("Funny Merge Balls", align="center", font=("Comic Sans MS", 35, "bold"))
            self.title.goto(0, (-self.canvas_height/2) + 120)
            self.title.color("#ffffff")
            self.title.write("Press 'space' to start!", align="center", font=("Comic Sans MS", 14, "bold"))

        self._score = 0
        self._game_over = False
        self.__start_val = False
        turtle.update()

    def invince(self, new_ball):
        for ball in self.ball_db:
            if new_ball == ball[0]:
                ball[2] = True

    def check_game_over(self):
        for ball in self.ball_db:
            if ball[0].ycor() + 2*self.property[ball[1]]["Radius"] >= 131 and ball[2]:
                self.__game_over()
                break

    def __game_over(self):
        self.__clear()

        self._game_over = True
        self.__start_val = False

        self.save_data()
        order_list = self.get_top(5)
        Sound().gameover.play()
        self.over_text.penup()
        self.over_text.goto(0,(self.canvas_height*0.325) - 30)
        self.over_text.color("#ff3030")
        self.over_text.write("GAMEOVER!!", align="center", font=("Comic Sans MS", 52, "bold"))
        self.over_text_left.penup()
        self.over_text_right.penup()
        self.over_text_restart.penup()
        self.over_text_restart.goto(0, (-self.canvas_height/2) + 150)
        self.over_text_restart.color("#ffffff")
        self.over_text_restart.write("Press 'space' to restart!", align="center", font=("Comic Sans MS", 14, "bold"))
        self.over_text_left.goto(-(self.canvas_width/2) + 90, self.over_text.ycor() - 50)
        self.over_text_right.goto((self.canvas_width/2) - 90, self.over_text.ycor() - 50)
        self.over_text_right.color("#ffffff")
        for data in order_list:
            data_name = data[0]
            data_score = data[1]
            if data[0] == self.username:
                self.over_text_left.color("#ff8c00")
                self.over_text_right.color("#ff8c00")
            else:
                self.over_text_left.color("#ffffff")
                self.over_text_right.color("#ffffff")
            self.over_text_left.goto(self.over_text_left.xcor(), self.over_text_left.ycor() - 25)
            self.over_text_right.goto(self.over_text_right.xcor(), self.over_text_right.ycor() - 25)
            self.over_text_left.write(f"({order_list.index(data) + 1}) {data_name}", align="left", font=("Comic Sans MS", 15, "bold"))
            self.over_text_right.write(f"{data_score}", align="right", font=("Comic Sans MS", 15, "bold"))

    def __space(self):
        if not self.__start_val:
            self.__start_val = True
            self._game_over = False
            self.__clear()
            self.__update_score()

            Sound().start.play()
            self.__border()
            self.__ui_ingame()
        else:
            Sound().drop.play()
            self.guild.clear()
            new_ball, state = self.ball_module.generate(random_property=self.random_num, origin=(self.dropper.posx, self.dropper.posy - 20))
            self.ball_db.append([new_ball, state, False])
            self.screen.ontimer(self.check_game_over)
            self.screen.ontimer(lambda:self.invince(new_ball), 600)

        self.random_num = random.randint(0,4)
        self.next_ball(self.property[self.random_num])
        turtle.update()

    def __clear(self):
        turtle.clear()
        self.score = 0
        self.title.clear()
        self.logo.hideturtle()
        self.exit_button.hideturtle()
        self.wall.clear()
        self.dropper.hide()
        self.score_text.clear()
        self.score_text.reset()
        self.score_text.hideturtle()
        self.Highscore_text.clear()
        self.guild.clear()
        self.over_text.clear()
        self.over_text_restart.clear()
        self.over_text_left.clear()
        self.over_text_right.clear()
        self.show_ball.clear()
        self.show_ball.hideturtle()

        while len(self.ball_db) != 0:
            for val in self.ball_db:
                val[0].clear()
                self.ball_db.remove(val)

        turtle.update()

    def run(self, _=None, __=None, ___=None):
        self._game_over = False
        self.__start_val = False
        self.__clear()

        self.__start()
        turtle.listen()
        turtle.onkey(self.__space, 'space')
        turtle.onkey(self.__game_over, 'o')

        turtle.done()
        self.save_data()