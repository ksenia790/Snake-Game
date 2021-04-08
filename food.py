from turtle import Turtle
import random

food_palette = ['magenta', 'DeepPink', 'MediumSlateBlue', 'DarkMagenta', 'Violet', 'HotPink', 'Orchid', 'MediumVioletRed']

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.7)
        self.color(random.choice(food_palette))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.color(random.choice(food_palette))
