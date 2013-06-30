from turtle import *
pendown()
bgcolor('black')
width(3)

color('red')
for i in range(3):
    fd(100)
    right(360/3)

color('white')
for i in range(4):
    fd(100)
    right(360/4)

color('blue')
for i in range(5):
    fd(100)
    right(360/5)

left(90)
for i in range(40):
    width(i)
    fd(4)

color('red')
width(3)
for i in range(36):
    fd(10)
    right(10)
