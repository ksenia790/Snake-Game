from turtle import Turtle
import  random

color_palette = ['GreenYellow', 'chartreuse', 'LawnGreen', 'Lime', 'DarkGreen', 'LimeGreen', 'Green', 'YellowGreen']
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    # create snake

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('black', random.choice(color_palette))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num-1].xcor()  # second last[1] segment position
            new_y = self.segments[segment_num - 1].ycor()  # second last segment[1] position
            self.segments[segment_num].goto(new_x, new_y)  # last segment[2] moves to the position of the segment [1]
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
