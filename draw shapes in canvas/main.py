import turtle # is a virtual library for canvas

# Createa canvas instance
myturtle = turtle.Turtle()

# Go to a certain coordinate
myturtle.penup() # donn't show pen
myturtle.goto(50, 75)

myturtle.pendown()
myturtle.forward(100) # Move 100 pixels
myturtle.left(90) # Turn 90 degrees left
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()