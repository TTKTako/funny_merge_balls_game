from Data import Balls_Data
from physic import physics_calculate
from playsound import playsound
import turtle
import time

class SetUp(Balls_Data):
    def __init__(self, username:str="Guest") -> None:
        super().__init__(username)

    def game_over(self):
        self.save_data()
        #TODO: clear scene and appear play again.