from Data import Balls_Data
import turtle
import time

class SetUp(Balls_Data):
    def __init__(self, username:str="Guest") -> None:
        super().__init__(username)