from turtle import *
pendown()
bgcolor('black')
width(3)
color('red')

def polygon(n):
    for i in range(n):
        fd(50)
        right(360.0/n)

polygon(5)

for i in range(3,10):
    polygon(i)

