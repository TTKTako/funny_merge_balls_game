import pandas as pd
import csv

class Balls_Data:
    def __init__(self, username:str="Guest") -> None:
        # only 5 balls in order that can be shoot from balls cannon
        # last balls will have a custom image
        self.property = [
            { #1
                "Radius": 5,
                "Color": "#fd9191",
                "Image": "/image/",
                "Reward": 300,
            },
            { #2
                "Radius": 8,
                "Color": "#9b9b9b",
                "Image": "/image/",
                "Reward": 15,
            },
            { #3
                "Radius": 10,
                "Color": "#cd69d4",
                "Image": "/image/",
                "Reward": 23,
            },
            { #4
                "Radius": 12,
                "Color": "#69d4b0",
                "Image": "/image/",
                "Reward": 36,
            },
            { #5
                "Radius": 15,
                "Color": "#658eb5",
                "Image": "/image/",
                "Reward": 41,
            },
            { #6
                "Radius": 20,
                "Color": "#65b569",
                "Image": "/image/",
                "Reward": 50,
            },
            { #7
                "Radius": 24,
                "Color": "#cfd131",
                "Image": "/image/",
                "Reward": 63,
            },
            { #8
                "Radius": 29,
                "Color": "#d16431",
                "Image": "/image/",
                "Reward": 75,
            },
            { #9
                "Radius": 33,
                "Color": "#d0f77e",
                "Image": "/image/",
                "Reward": 90,
            },
            { #10
                "Radius": 39,
                "Color": "#d0f77e",
                "Image": "/image/",
                "Reward": 115,
            },
            { #11
                "Radius": 45,
                "Color": "#272e5d",
                "Image": "/image/",
                "Reward": 155,
            },
            { #12
                "Radius": 55,
                "Color": "#0e1021",
                "Image": "/image/",
                "Reward": 220,
            },
        ]

        self.Balls_db = []
        self.username = username
        self._score = 0

    def __get_data(self):
        with open("datafile.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)

            for i in csv_reader:
                if i['Name'].strip() == self.username:
                    return i['Score']
            return 0

    @property
    def highscore(self):
        self._past_highscore = self.__get_data()
        return self._past_highscore