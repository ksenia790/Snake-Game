from turtle import Turtle

POSITION_Y = 270
POSITION_X = 0

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.setposition(POSITION_X, POSITION_Y)
        self.current_scores = 0
        with open("data.txt") as data:
            hight_score = int(data.read())
        self.highest_score = hight_score
        self.write(arg=f"Scores: {self.current_scores} Hight Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Scores: {self.current_scores}  Hight Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_scores > self.highest_score:
            self.highest_score = self.current_scores
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highest_score}")
        self.current_scores = 0

    def increase_scores(self):
        self.current_scores += 1
        self.update_scoreboard()

