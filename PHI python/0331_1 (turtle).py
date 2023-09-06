#*은 전부 다 라는 의미를 가지고 있음
#from turtle import *

'''
for a in range(4):
    forward(100)
    right(90)

for b in range(3):
    forward(150)
    right(120)

for c in range(5):
    forward(180)
    right(72)

for d in range(5):
    forward(200)
    right(144)
'''


'''

import turtle as t

t.shape("arrow")

t.pensize(4)

t.penup()
t.goto(0, -200)
t.pendown()
t.circle(40, steps = 3)

t.penup()
t.goto(0,-100)
t.pendown()
t.circle(40, steps = 4)

t.penup()
t.goto(0,0)
t.pendown()
t.circle(40, steps = 5)

t.penup()
t.goto(0, 100)
t.pendown()
t.circle(40)

t.penup()
t.goto(-40, 260)
t.pendown()
for x in range(5):
    t.forward(80)
    t.right(144)
'''





import turtle as t

t.shape("circle")
t.color("pink")
t.bgcolor("skyblue")
t.speed(0)
t.shapesize(2,2)#거북이 사이즈 바꾸기
t.pensize(4)
t.circle(50, steps = 4)#(크기, 구성 선분의 수)
t.goto(0, 0)
t.clear()


t.penup()
t.goto(-200, -50)
t.pendown()
t.circle(40, steps = 3)

t.penup()
t.goto(-100, -50)
t.pendown()
t.circle(40, steps = 4)

t.penup()
t.goto(0, -50)
t.pendown()
t.circle(40, steps = 5)

t.penup()
t.goto(100, -50)
t.pendown()
t.circle(40)


