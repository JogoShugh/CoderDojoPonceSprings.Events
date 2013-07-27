from turtle import *
pendown()
bgcolor('black')
width(3)

def circle():
    for i in range(36):
        fd(10)
        right(10)

color_list=['red', 'green', 'blue', 'purple', 'orange', 'yellow']
for item in color_list:
    color(item)
    circle()
    right(60)

