
import turtle

turtle.bgcolor('#ba161e') #Dark Red
turtle.speed(2)
t = turtle.Turtle()
turtle.hideturtle()

t.penup()
t.setposition(0, 120)
t.pendown()

# top
t.begin_fill()
t.fillcolor('#fab104')
p1 = [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20),(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
for pos in p1:
    x, y = pos 
    t.setposition(x, y)
t.end_fill()

t.penup()
t.setposition(0, -30)
t.pendown()

#middle
t.begin_fill()
t.fillcolor('#fab104')
p2 = [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210),(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
for pos in p2:
    x, y = pos 
    t.setposition(x, y)
t.end_fill()

t.penup()
t.setposition(0, -220)
t.pendown()
# bottom
t.begin_fill()
t.fillcolor('#fab104')
p3 = [(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250),(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220),(0, -220)]
for pos in p3:
    x, y = pos 
    t.setposition(x, y)
t.end_fill()

turtle.hideturtle()
turtle.done()