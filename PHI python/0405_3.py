import turtle as t
from random import *
t.bgcolor("khaki")

c = ["crimson", "maroon", "darkorange", "olive", "teal", "steelblue", \
     "dodgerblue", "mediumblue"]


def draw3(angle):
    d = 1
    for i in range(100):
        t.fd(d)
        t.rt(angle)
        d += 2

t.speed(0)
loop = "y"


while (loop == "y"):
    angle = input("터틀이 회전할 각도 입력: ")
    t.color(c[randint(0, 7)])
    draw3(int(angle))
    loop = input("계속하려면 y, 멈추려면 n을 입력하세요.")

    if (loop == "n"):
        break

    elif loop == "y":
        t.penup()
        t.goto(randint(-300, 300), randint(-300, 300))
        t.pendown()
