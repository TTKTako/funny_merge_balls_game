"""This module is for store sound only."""

from pygame import mixer

class Sound:
    """
    store all the game sound into pygame.
    """
    def __init__(self):
        mixer.init()
        self.start = mixer.Sound("start.wav")
        self.gameover = mixer.Sound("gameover.wav")
        self.merge = mixer.Sound("merge.wav")
        self.drop = mixer.Sound("drop.wav")
