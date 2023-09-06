import turtle as t
t.speed(0)


'''
for count in range(10):
    line = input("삼각형을 그리고 싶다면 3,\
    \n사각형을 그리고 싶다면 4, \
    \n오각형을 그리고 싶다면 5, \
    \n육각형을 그리고 싶다면 6, \
    \n별을 그리고 싶다면 7, \
    \n원을 그리고 싶다면 1을 입력하세요: ")

    if line == "3":
        t.circle(50, steps = 3)

    elif line == "4":
        t.circle(50, steps = 4)

    elif line == "5":
        t.circle(50, steps = 5)

    elif line == "6":
        t.circle(50, steps = 6)

    elif line == "7":
        for star in range(5):
            t.fd(100)
            t.rt(144)

    elif line == "1":
        t.circle(50)

    else:
        print("올바른 응답이 아닙니다.")
'''
#
'''
c = ["red", "yellow", "green", "blue", "purple"]

for x in range(len(c)):
    t.color(c[x])
    size = (x + 1) * 50
    t.circle(size)
'''
#



c = ["red", "purple", "hotpink", "pink", "silver"]

t.penup()
t.goto(0, -200)
t.pendown()

def draw1():
    for x in range(len(c)):
        t.color(c[x])
        size = (x + 1) * 50
        t.circle(size)

def draw2():
    for x in range(len(c)):
        t.fillcolor(c[x])
        t.begin_fill()
        size = (len(c) - x) * 50
        t.circle(size)
        t.end_fill()

















