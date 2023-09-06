import turtle as t

'''
t.fillcolor("blue")#채우기 색 지정
t.begin_fill()#채우기 시작
t.circle(50, steps = 5)
t.end_fill()#채우기 끝, end_fill()을 실행 할 때 색이 채워짐

t.color("red", "purple")#(펜 색, 채우기 색), 채우기 색 지정 안하면 거북이의 색으로 채움
t.penup()
t.goto(-100, -100)
t.pendown()
t.pensize(4)
t.begin_fill()#지금부터 그리는 것을 채움
for x in range(5):
    t.fd(200)
    t.rt(144)
t.end_fill()


t.rt(1)
t.goto(0, 0)
t.clear()
'''
'''
t.fillcolor(1, 0, 1)
t.penup()#pendown() 안해도 채우기 가능
t.goto(-200, 0)
t.begin_fill()
t.circle(50)
t.end_fill()

t.fillcolor(1, 0.5, 0)
t.goto(0, 0)
t.begin_fill()
t.circle(50)
t.end_fill()

t.fillcolor(0, 1, 0.3)
t.goto(200, 0)
t.begin_fill()
t.circle(50)
t.end_fill()
'''

t.colormode(255)#255범위로 rgb색 정하기
t.fillcolor(255, 203, 255)
t.penup()
t.goto(-200, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()

t.colormode(255)
t.fillcolor(255, 152, 255)
t.penup()
t.goto(-100, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()

t.colormode(255)
t.fillcolor(255, 101, 255)
t.penup()
t.goto(0, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()

t.colormode(255)
t.fillcolor(255, 63, 255)
t.penup()
t.goto(100, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()

t.colormode(255)
t.fillcolor(255, 0, 255)
t.penup()
t.goto(200, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()


t.colormode(255)
t.fillcolor("#FF0099")#16진수로 넣을 때는 문자와 #이 들어감
t.penup()
t.goto(300, 0)
t.begin_fill()
t.circle(50)
t.pendown()
t.end_fill()

