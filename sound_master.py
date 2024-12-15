from pygame import mixer

class sound:
    def __init__(self):
        mixer.init()
        self.start = mixer.Sound("start.wav")
        self.gameover = mixer.Sound("gameover.wav")
        self.merge = mixer.Sound("merge.wav")
        self.drop = mixer.Sound("drop.wav")