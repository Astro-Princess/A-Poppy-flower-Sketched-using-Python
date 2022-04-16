from turtle import *

speed(0)
color("#E35335")

def flower():
    for i in range(300):
        circle(190-i, 90)
        left(90)
        circle(190-i, 90)
        left(18)

flower()

hideturtle()
