from turtle import Turtle,Screen
import turtle
s=Screen()
s.bgcolor("black")
k=Turtle()
k.hideturtle()
k.speed(0)
clr=['red', 'blue', 'green', 'yellow', 'orange']
for i in range(3600):
	k.color(clr[i%5])
	k.circle(220,360)
	k.left(3)
	
turtle.mainloop()
