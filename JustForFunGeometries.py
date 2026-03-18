# Johans Nurkka
# March 15, 2026
# P4LAB1
# Turtle Geometries

import turtle

win = turtle.Screen()
t = turtle.Turtle()
t.speed(3)
t.color("purple")
t.shape("turtle")

rotation = 0

while rotation != 360:
    for side in range (4):
        t.forward(200)
        t.left(90)
    t.left(7)
    rotation += 7