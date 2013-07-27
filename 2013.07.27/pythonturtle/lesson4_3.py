from turtle import *
pendown()
bgcolor('black')
width(3)
color('red')

def polygon(n):
    for i in range(n):
        fd(50)
        right(360.0/n)


for i in range(3,15):
    polygon(i)
    right(30)

