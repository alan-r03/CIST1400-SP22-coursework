import turtle
import random
franklin = turtle.Turtle()
size = 60
franklin.speed(500)
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
x = 0

for i in range(500):
    franklin.color(colors[x%6])
    for j in range(3):
        franklin.forward(size)
        franklin.right(120)
    franklin.right(3)
    x += 1
    size += 1
