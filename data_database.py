"""This code is used for manage database don't modifired."""

import csv
import pandas as pd

class BallsDB:
    """
    This class will access the file call 'datafile.csv'
    Do not change the file name or header of the file!!
    """

    def __init__(self, username:str="Guest") -> None:
        # only 5 balls in order that can be shoot from balls cannon
        # every balls will be a emoji
        self.property = [
            { #1
                "Radius": 10,
                "Color": "#fd9191",
                "Image": "/image/",
                "Reward": 500,
            },
            { #2
                "Radius": 12,
                "Color": "#9b9b9b",
                "Image": "/image/",
                "Reward": 15,
            },
            { #3
                "Radius": 14,
                "Color": "#cd69d4",
                "Image": "/image/",
                "Reward": 23,
            },
            { #4
                "Radius": 17,
                "Color": "#69d4b0",
                "Image": "/image/",
                "Reward": 36,
            },
            { #5
                "Radius": 19,
                "Color": "#658eb5",
                "Image": "/image/",
                "Reward": 41,
            },
            { #6
                "Radius": 23,
                "Color": "#65b569",
                "Image": "/image/",
                "Reward": 50,
            },
            { #7
                "Radius": 27,
                "Color": "#cfd131",
                "Image": "/image/",
                "Reward": 63,
            },
            { #8
                "Radius": 32,
                "Color": "#d16431",
                "Image": "/image/",
                "Reward": 75,
            },
            { #9
                "Radius": 36,
                "Color": "#d0f77e",
                "Image": "/image/",
                "Reward": 90,
            },
            { #10
                "Radius": 42,
                "Color": "#d0f77e",
                "Image": "/image/",
                "Reward": 115,
            },
            { #11
                "Radius": 48,
                "Color": "#272e5d",
                "Image": "/image/",
                "Reward": 155,
            },
            { #12
                "Radius": 58,
                "Color": "#0e1021",
                "Image": "/image/",
                "Reward": 220,
            },
        ]

        self.ball_db = []
        self.username = username
        self._score = 0
        self.__file = "datafile.csv"
        self._past_highscore = self.__get_data()

    def __get_data(self):
        with open(self.__file, mode="r", encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for i in csv_reader:
                if i['Name'].strip() == self.username:
                    return i['Score']
            return 0

    def save_data(self):
        """
        this function will save the player data from the player username
        """
        check = bool(self.__get_data())
        if check:
            if self._score > int(self.highscore):
                rows = []
                with open(self.__file, mode="r", newline="", encoding='utf-8') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    rows.append(headers)

                    for row in reader:
                        if row[0] == self.username:
                            row[1] = str(self._score)
                        rows.append(row)

                with open(self.__file, mode="w", newline="", encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
        else:
            new_row = [self.username, self._score]
            with open(self.__file, mode="a", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(new_row)

    def get_top(self, val:int = 5):
        """
        get top n of the datafile.csv
        """
        file = pd.read_csv(self.__file)
        top = file.nlargest(val, 'Score')
        top_list = top[['Name', 'Score']].values.tolist()
        if len(top_list) - val != 0:
            for _ in range(val - len(top_list)):
                top_list.append(["------", "---"])
        return top_list

    @property
    def highscore(self):
        """
        this getter will automatically pull data from the csv file.
        """
        self._past_highscore = self.__get_data()
        return self._past_highscore
