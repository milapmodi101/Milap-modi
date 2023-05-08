import turtle
a=turtle.Turtle()
a.color("cyan")
a.speed(0)
a.hideturtle()

s=turtle.Screen()
s.bgcolor("black")

for y in range (210):
	a.forward(y)
	a.left(y-1)
turtle.done()
	