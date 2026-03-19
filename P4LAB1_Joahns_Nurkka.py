# Johans Nurkka
# March 15, 2026
# P4LAB1
# Turtle Geometries uses turtle graphics to illustrate a triangle arranged on top of a square

'''
1) Import turtle graphics
2) Define the terminal workspace
3) Define turtle one parameters
4) Define turtle two parameters
5) Define while loop; condition = the # of sides; exit criteria = sides +=1
6) Define the triangle dimensions
7) Define for loop; variable = # of sides; range = 4 (# sides in a quadrilateral)
8) Define the square dimensions
9) Exit on click to prevent window from closing for review
'''

# Import turtle graphics
import turtle

# Define the terminal workspace
win = turtle.Screen()
win.bgcolor("slategray")
win.title("Turtle Power")

# Define turtle one parameters: speed, line color, and fill color
donnie = turtle.Turtle()
donnie.speed(3)
donnie.pencolor("blue")
donnie.fillcolor("purple")

# Define turtle two parameters: speed, line color, and fill color
mikey = turtle.Turtle()
mikey.speed(8)
mikey.pencolor("yellow")
mikey.fillcolor("orange")

# Make the triangle
# Set the start point for the fill color
# Define the while loop; condition = tri_side = 0; exit criteria = 0 += 1
# Triangle dimensions: side length = 200; outside angle = 120
# Mark the end point for color fill
donnie.begin_fill()
tri_side = 0
while tri_side < 3:
    donnie.forward(200)
    donnie.left(120)
    tri_side += 1
donnie.end_fill()

# Make the square
# Set start point for the fill color
# Define the for loop; variable = sq_side; range = 4
# Square dimensions: side length = 200; outside angle = 90
# Mark the end point for color fill
mikey.begin_fill()
for sq_side in range(4):
    mikey.forward(200)
    mikey.right(90)
mikey.end_fill()

# Exit on click to keep terminal open for review
win.exitonclick()