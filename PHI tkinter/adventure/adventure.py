import tkinter
import random
import math


stage = 0
background = 0

canvas_width = 636


#맵에 원 생성 및
r = 25
x1 = 456
y1 = 768
x2 = 124
y2 = 692
x3 = 346
y3 = 414
x4 = 114
y4 = 207
x5 = 515
y5 = 150
x6 = 515
y6 = 24
c1 = "yellow"
c2 = "yellow"
c3 = "yellow"
c4 = "yellow"
c5 = "yellow"
c6 = "yellow"

def draw_circle(x, y, color):
    global r
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = color, tag="SCREEN")


#마우스
def mouse_click(e):
    global stage
    print(e.x, e.y)
    if stage == 0: #타이틀에서 벗어남(1회용)
        stage = 1

def mouse_cancel(e):
    a=0

def mouse_move(e):
    global x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6, r
    if stage == 1: #맵 원 거리 체크
        x = e.x
        y = e.y
        dis1 = math.sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))#1
        if dis1 <= r:
            c1 = "white"
        else:
            c1 = "yellow"
        dis2 = math.sqrt((x2-x)*(x2-x) + (y2-y)*(y2-y))#2
        if dis2 <= r:
            c2 = "white"
        else:
            c2 = "yellow"
        dis3 = math.sqrt((x3-x)*(x3-x) + (y3-y)*(y3-y))#3
        if dis3 <= r:
            c3 = "white"
        else:
            c3 = "yellow"
        dis4 = math.sqrt((x4-x)*(x4-x) + (y4-y)*(y4-y))#4
        if dis4 <= r:
            c4 = "white"
        else:
            c4 = "yellow"
        dis5 = math.sqrt((x5-x)*(x5-x) + (y5-y)*(y5-y))#5
        if dis5 <= r:
            c5 = "white"
        else:
            c5 = "yellow"
        dis6 = math.sqrt((x6-x)*(x6-x) + (y6-y)*(y6-y))#6
        if dis6 <= r:
            c6 = "white"
        else:
            c6 = "yellow"
        draw_background(background)
        draw_circle(x1, y1, c1)
        draw_circle(x2, y2, c2)
        draw_circle(x3, y3, c3)
        draw_circle(x4, y4, c4)
        draw_circle(x5, y5, c5)
        draw_circle(x6, y6, c6)


#텍스트
def draw_txt(txt, x, y, size, color):
    fnt = ("Arial", size)
    canvas.create_text(x, y, text = txt, fill = color, font = fnt, tag="SCREEN")


#배경
def draw_background(bg):
    canvas.delete("SCREEN")
    canvas.create_image(636/2, 900/2, image = background_img[bg], tag="SCREEN")

#화면
def draw_screen():
    canvas.delete("SCREEN")


#메인
def main():
    global stage, background

    canvas.bind("<Button-1>", mouse_click) #좌클릭
    canvas.bind("<Button-2>", mouse_cancel) #우클릭
    canvas.bind("<Motion>", mouse_move) #마우스 움직임

    if stage == 0: #타이틀
        draw_background(stage)
        draw_txt("ADVENTURE", 636/2, 100, 70, "hotpink")
        draw_txt("click to start", 632/2, 750, 40, "yellow")


    elif stage == 1: #맵
        background = 0
        draw_background(background)
        draw_circle(x1, y1, c1)
        draw_circle(x2, y2, c2)
        draw_circle(x3, y3, c3)
        draw_circle(x4, y4, c4)
        draw_circle(x5, y5, c5)
        draw_circle(x6, y6, c6)


    tkt.after(100, main) #반복시킴


#기본 설정
tkt = tkinter.Tk()
tkt.title("adventure")
tkt.resizable(False, False) #가로세로 크기 변경 불가
canvas = tkinter.Canvas(width = canvas_width, height = 900)
canvas.pack()


#이미지
character_img = [
    tkinter.PhotoImage(file="adventure_img/character00.png"),
    tkinter.PhotoImage(file="adventure_img/character01.png"),
    tkinter.PhotoImage(file="adventure_img/character02.png"),
    tkinter.PhotoImage(file="adventure_img/character03.png")
    ]

background_img = [
    tkinter.PhotoImage(file="adventure_img/map.png"),
    tkinter.PhotoImage(file="adventure_img/forest.png"),
    tkinter.PhotoImage(file="adventure_img/shop_background.png"),
    tkinter.PhotoImage(file="adventure_img/card_shop.png"),
    tkinter.PhotoImage(file="adventure_img/beach.png"),
    tkinter.PhotoImage(file="adventure_img/castle.png"),
    tkinter.PhotoImage(file="adventure_img/throne.png")
    ]

card_attack_img = [
    tkinter.PhotoImage(file="adventure_img/card_attack00.png"),
    tkinter.PhotoImage(file="adventure_img/card_attack01.png")
    ]

card_shield_img = [
    tkinter.PhotoImage(file="adventure_img/card_shield00.png"),
    tkinter.PhotoImage(file="adventure_img/card_shield01.png")
    ]

card_heal_img = [
    tkinter.PhotoImage(file="adventure_img/card_heal00.png"),
    tkinter.PhotoImage(file="adventure_img/card_heal01.png")
    ]

shop_img = [
    tkinter.PhotoImage(file="adventure_img/shop00.png"),
    tkinter.PhotoImage(file="adventure_img/shop01.png")
    ]

round_void_img = [
    tkinter.PhotoImage(file="adventure_img/round_void00.png"),
    tkinter.PhotoImage(file="adventure_img/round_void01.png")
    ]

round_attack_img = [
    tkinter.PhotoImage(file="adventure_img/round_attack00.png"),
    tkinter.PhotoImage(file="adventure_img/round_attack01.png")
    ]

round_shield_img = [
    tkinter.PhotoImage(file="adventure_img/round_shield00.png"),
    tkinter.PhotoImage(file="adventure_img/round_shield01.png")
    ]

round_heal_img = [
    tkinter.PhotoImage(file="adventure_img/round_heal00.png"),
    tkinter.PhotoImage(file="adventure_img/round_heal01.png")
    ]

monster_img = [
    tkinter.PhotoImage(file="adventure_img/slime_forest.png"),
    tkinter.PhotoImage(file="adventure_img/slime_beach.png"),
    tkinter.PhotoImage(file="adventure_img/slime_castle.png"),
    tkinter.PhotoImage(file="adventure_img/slime_king.png")
    ]


#반복
main()
tkt.mainloop()
