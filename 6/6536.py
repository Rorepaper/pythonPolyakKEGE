from turtle import *


def f(n):
    forward(n*k)


speed(10)
k = 40
left(90)
for _ in "...":
    f(4)
    left(270)
    f(7)
    right(90)
left(315)
for _ in "....":
    f(7)
    right(90)
    f(4)
    left(270)
up()
for x in range(-10*k, 10*k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x, y)
        if y == 0:
            dot(5, "green")
        else:
            dot(5, "red")

done()
