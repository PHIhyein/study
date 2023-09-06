import turtle as t


def tree(w):
    if w >= 10:
        t.fd(w)
        t.rt(30)
        tree(w - 2.5)
        t.lt(60)
        tree(w - 2.5)
        t.rt(30)
        t.bk(w)

t.speed(0)
t.goto(0, -90)

t.color("brown")
t.pensize(10)
t.lt(90)
t.fd(90)
t.color("yellowgreen")
t.pensize(2)


tree(30)














'''
#
def tree(w):
    if w >= 10:
        t.fd(w)#30, 27.5, 25, 22.5, 20, 17.5, 15, 12.5, 10, 7.5, 5
        t.rt(30)
        tree(w - 2.5)#작아지다가/2.5되면 멈춤->w=5/7.5에서 tree(5)가 하나 더 생김
        t.lt(60)#10번 정도 반복하고 회전
        tree(w - 2.5)#커짐/w=5에서 반응 없음->w=5
        t.rt(30)
        t.bk(w)
'''
