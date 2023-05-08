import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.width(2)
tur.bgcolor("black")
tur.speed(0)
tur.tracer(10)

def square(x):
       for i in range(4):
             tur.forward(x)
             tur.left(90)

for j in range(30):
      for i in range(15):
            tur.color(cs.hsv_to_rgb(i/14,j/29,1))
            tur.right(135)
            square(200-j*2)
            tur.left(135)
            tur.circle(50,24)

tur.done()


