import math
import random
import turtle
import time


def fib(x, d=None):
    if d == None:
        d = [False]*(x+1)

    if d[x] == False:
        if x == 1:
            d[x] = 1
            return d[x]
        elif x == 0:
            d[x] = 1
            return d[x]
        d[x] = fib(x-1, d) + fib(x-2, d)
        return d[x]
    return d[x]


def drowFib(numbers, color='blue', shape='arrow', pensize=3, speed=50, step=15, fibsteps=500, start=(0, 0)):
    '''
    this function visualize the modulus of the Fibonacci Series over a number
    nembers is one number or list of numbers
    '''

    window = turtle.Screen()
    window.setup(width=1.0, height=1.0, startx=None, starty=None)

    if (type(numbers) != type([])):
        numbers = [numbers]
    turtles = [turtle.Turtle() for _ in range(len(numbers))]

    for t in turtles:
        t.color(color)
        t.pensize(pensize)
        t.shape(shape)
        t.speed(speed)
        t.penup()
        t.goto(start[0], start[1])
        t.pendown()
        # t.right(135)

    for number in range(0, fibsteps):
        f = fib(number)

        for index in range(len(turtles)):
            r = f % numbers[index]
            if r == 0:
                pass
            elif (r % 2) == 0:
                turtles[index].right(90)
                turtles[index].forward(step)
            else:
                turtles[index].left(90)
                turtles[index].forward(step)
    time.sleep(2)


# drowFib(13)
