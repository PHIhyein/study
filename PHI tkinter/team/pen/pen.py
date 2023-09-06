import tkinter
import random


key= ""
koff = False
def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global key
    key = ""

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]
BLINK = ["#fff", "#ffc", "#ff8", "#fe4", "#ff8", "#ffc"]

idx = 0
tmr = 0
stage = 1
candy = 0
nokori = 3
score = 0

pen_x = 0
pen_y = 0
pen_d = 0
pen_a = 0

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0
red_sy = 0

red1_x = 0
red1_y = 0
red1_d = 0
red1_a = 0
red1_sx = 0
red1_sy = 0
red1_sd = 0

kuma_x = 0
kuma_y = 0
kuma_d = 0
kuma_a = 0
kuma_sx = 0
kuma_sy = 0
kuma_sd = 0

kuma1_x = 0
kuma1_y = 0
kuma1_d = 0
kuma1_a = 0
kuma1_sx = 0
kuma1_sy = 0
kuma1_sd = 0

mario_x = 0
mario_y = 0
mario_d = 0
mario_a = 0
mario_sx = 0
mario_sy = 0
mario_sd = 0

map_data = []

def set_stage():
    global map_data, candy
    global pen_sx, pen_sy
    global red_sx, red_sy
    global red1_sx, red1_sy, red1_sd
    global kuma_sx, kuma_sy, kuma_sd
    global kuma1_sx, kuma1_sy, kuma1_sd
    global mario_sx, mario_sy, mario_sd
    if stage == 1:
        map_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 3, 2, 2, 0],
            [0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 3, 2, 2, 2, 0, 3, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 0, 3, 2, 2, 2, 0, 3, 2, 2, 2, 0],
            [0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 3, 2, 2, 2, 0, 3, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0, 0, 3, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0],
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        candy = 31
        pen_sx = 90
        pen_sy = 510
        red_sx = 1050
        red_sy = 500
        red1_sd = -1
        kuma_sd = -1
        kuma1_sd = -1
        mario_sd = -1


    if stage == 2:
        map_data = [
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,0,0,2,2,0,1,1,1,2,1,1,1,0,2,2,2,0,0,2,2,0],
            [0,2,2,1,1,2,0,1,3,3,3,0,3,3,3,1,0,2,2,1,1,2,2,0],
            [0,2,2,2,2,0,1,3,3,3,3,0,3,3,3,3,1,0,2,2,2,2,2,0],
            [0,2,2,2,0,1,3,3,2,2,3,1,3,2,2,3,3,1,0,2,2,2,2,0],
            [0,2,2,2,0,3,3,2,2,2,3,3,3,2,2,2,3,3,0,2,2,2,2,0],
            [0,2,2,2,0,3,3,2,2,2,2,2,2,2,2,2,3,3,0,2,2,2,2,0],
            [0,2,2,2,0,3,3,2,2,2,2,2,2,2,2,2,3,3,0,2,2,2,2,0],
            [0,2,2,2,1,0,3,3,2,2,2,2,2,2,2,3,3,0,1,2,2,2,2,0],
            [0,2,2,2,2,1,0,3,3,2,2,2,2,2,3,3,0,1,2,2,2,2,2,0],
            [0,2,2,2,2,2,1,0,3,3,2,2,2,3,3,0,1,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,1,0,3,3,3,3,3,0,1,2,2,2,2,2,2,2,0],
            [0,2,2,0,0,2,2,2,1,0,3,3,3,0,1,2,2,2,2,0,0,2,2,0],
            [0,2,2,1,1,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]
        candy = 55
        pen_sx = 450
        pen_sy = 400
        red_sx = 630
        red_sy = 450
        red1_sd = 1
        red1_sx = 990
        red1_sy = 560
        kuma_sd = -1
        mario_sd = -1
        

    if stage == 3:
        map_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 0, 0, 0, 3, 3, 0, 0, 3, 2, 2, 2, 2, 3, 0, 0, 3, 3, 0, 0, 0, 3, 0],
            [0, 3, 0, 0, 0, 3, 3, 3, 3, 2, 2, 0, 0, 2, 2, 3, 3, 3, 3, 0, 0, 0, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 3, 3, 3, 3, 0, 3, 3, 2, 2, 0, 0, 2, 2, 3, 3, 0, 3, 3, 3, 3, 3, 0],
            [0, 3, 3, 3, 0, 3, 0, 0, 3, 3, 2, 2, 2, 2, 3, 3, 0, 0, 3, 0, 3, 3, 3, 0],
            [0, 3, 0, 0, 0, 3, 3, 0, 0, 3, 2, 2, 2, 2, 3, 0, 0, 3, 3, 0, 0, 0, 3, 0],
            [0, 3, 3, 2, 0, 2, 2, 2, 0, 3, 2, 2, 2, 2, 3, 0, 2, 2, 2, 0, 2, 3, 3, 0],
            [0, 0, 0, 2, 0, 2, 2, 2, 0, 3, 0, 0, 0, 0, 3, 0, 2, 2, 2, 0, 2, 0, 0, 0],
            [0, 3, 0, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 0, 3, 0],
            [0, 3, 2, 2, 0, 0, 0, 0, 3, 3, 2, 0, 0, 2, 3, 3, 0, 0, 0, 0, 2, 2, 3, 0],
            [0, 3, 2, 2, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 2, 2, 3, 0],
            [0, 3, 0, 2, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 0, 2, 0, 3, 0],
            [0, 3, 0, 2, 0, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 2, 0, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        candy = 166
        pen_sx = 690
        pen_sy = 450
        red_sx = 390
        red_sy = 450
        red1_sd = 1
        red1_sx = 990
        red1_sy = 560
        kuma_sd = 1
        kuma_sx = 1350
        kuma_sy = 250
        kuma_sd = DIR_DOWN
        kuma1_sd = 1
        kuma1_sx = 1290
        kuma1_sy = 270
        kuma1_sd = DIR_RIGHT

        mario_sd = 1
        mario_sx = 90
        mario_sy = 90
        mario_sd = DIR_RIGHT
        
       
def set_chara_pos():
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    global red1_x, red1_y, red1_d, red1_a
    global kuma_x, kuma_y, kuma_d, kuma_a
    global kuma1_x, kuma1_y, kuma1_d, kuma1_a
    global mario_x, mario_y, mario_d, mario_a
    pen_x = pen_sx
    pen_y = pen_sy
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = red_sx
    red_y = red_sy
    red_d = DIR_DOWN
    red_a = 3
    red1_x = red1_sx
    red1_y = red1_sy
    red1_d = red1_sd
    red1_a = 0
    kuma_x = kuma_sx
    kuma_y = kuma_sy
    kuma_d = kuma_sd
    kuma_a = 0
    kuma1_x = kuma1_sx
    kuma1_y = kuma1_sy
    kuma1_d = kuma1_sd
    kuma1_a = 0
    mario_x = mario_sx
    mario_y = mario_sy
    mario_d = mario_sd
    mario_a = 0


def draw_txt(txt, x, y, siz, col):
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag="SCREEN")
    canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")


def draw_screen():
    canvas.delete("SCREEN")
    for y in range(17):
        for x in range(24):
            canvas.create_image(x * 60 + 30, y * 60 + 30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN")
    if red1_sd != -1:
        canvas.create_image(red1_x, red1_y, image=img_red1[red1_a], tag="SCREEN")
    if kuma_sd != -1:
        canvas.create_image(kuma_x, kuma_y, image=img_kuma[kuma_a], tag="SCREEN")
    if kuma1_sd != -1:
        canvas.create_image(kuma1_x, kuma1_y, image=img_kuma1[kuma1_a], tag="SCREEN")
    if mario_sd != -1:
        canvas.create_image(mario_x, mario_y, image=img_mario[mario_a], tag="SCREEN")
    draw_txt("SCORE" + str(score), 150, 30, 30, "white")
    draw_txt("STAGE" + str(stage), 1300, 30, 30, "lime")
    for i in range(nokori):
        canvas.create_image(60 + i * 50 ,900,image=img_pen[12], tag="SCREEN")

def check_wall(cx, cy, di, dot):
    chk = False
    if di == DIR_UP:
        mx = int((cx - 30)/ 60)
        my = int((cy - 30 - dot) / 60)
        if map_data[my][mx] <= 1:
            chk = True
        mx = int((cx + 29)/ 60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_DOWN:
        mx = int((cx - 30)/60)
        my = int((cy + 29 + dot) / 60)
        if map_data[my][mx] <= 1:
            chk = True
        mx = int((cx + 29)/ 60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_LEFT:
        mx = int((cx - 30 - dot)/60)
        my = int((cy - 30)/ 60)
        if map_data[my][mx] <= 1:
            chk=True
        my = int((cy + 29)/ 60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx + 29 + dot) / 60)
        my = int((cy - 30)/ 60)
        if map_data[my][mx] <= 1:
            chk =True
        my = int((cy + 29)/ 60)
        if map_data[my][mx] <= 1:
            chk = True
    return chk

def move_penpen():
    global pen_x, pen_y, pen_d, pen_a, score, candy
    speed = 15
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x,pen_y, pen_d, 20) == False:
            pen_y = pen_y -20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x,pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x,pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x,pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d * 3 + ANIMATION[tmr % 4]
    mx = int(pen_x / 60)
    my = int(pen_y / 60)
    if map_data[my][mx] == 3:
        score = score + 100
        map_data[my][mx] =2
        candy = candy - 1

def move_enemy():
    global red_x, red_y, red_d, red_a, idx, tmr
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:
        red_d = random.randint(0,6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d * 3 + ANIMATION[tmr % 4]
    if abs(red_x - pen_x) <= 40 and abs(red_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy2():
    global kuma_x, kuma_y, kuma_d, kuma_a, idx, tmr
    speed = 10
    if kuma_sd == -1:
        return
    if kuma_d == DIR_UP:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y - speed
        else:
            kuma_d = DIR_DOWN
    elif kuma_d == DIR_DOWN:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y + speed
        else:
            kuma_d = DIR_UP
    elif kuma_d == DIR_LEFT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x - speed
        else:
            kuma_d = DIR_RIGHT
    elif kuma_d == DIR_RIGHT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x + speed
        else:
            kuma_d = DIR_LEFT
    kuma_a = ANIMATION[tmr % 4]
    if abs(kuma_x - pen_x) <= 40 and abs(kuma_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy3():
    global red1_x, red1_y, red1_d, red1_a, idx, tmr
    speed = 10
    if red1_sd == -1:
        return
    if red1_x % 60 == 30 and red1_y % 60 == 30:
        red1_d = random.randint(0,6)
        if red1_d >= 4:
            if pen_y < red1_y:
                red1_d = DIR_UP
            if pen_y > red1_y:
                red1_d = DIR_DOWN
            if pen_x < red1_x:
                red1_d = DIR_LEFT
            if pen_x > red1_x:
                red1_d = DIR_RIGHT
    if red1_d == DIR_UP:
        if check_wall(red1_x, red1_y, red1_d, speed) == False:
            red1_y = red1_y - speed
    if red1_d == DIR_DOWN:
        if check_wall(red1_x, red1_y, red1_d, speed) == False:
            red1_y = red1_y + speed
    if red1_d == DIR_LEFT:
        if check_wall(red1_x, red1_y, red1_d, speed) == False:
            red1_x = red1_x - speed
    if red1_d == DIR_RIGHT:
        if check_wall(red1_x, red1_y, red1_d, speed) == False:
            red1_x = red1_x + speed
    red1_a = red1_d * 3 + ANIMATION[tmr % 4]
    if abs(red1_x - pen_x) <= 40 and abs(red1_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy4():
    global kuma1_x, kuma1_y, kuma1_d, kuma1_a, idx, tmr
    speed = 5
    if kuma1_sd == -1:
        return
    if kuma1_d == DIR_UP:
        if check_wall(kuma1_x, kuma1_y, kuma1_d, speed) == False:
            kuma1_y = kuma1_y - speed
        else:
            kuma1_d = DIR_DOWN
    elif kuma1_d == DIR_DOWN:
        if check_wall(kuma1_x, kuma1_y, kuma1_d, speed) == False:
            kuma1_y = kuma1_y + speed
        else:
            kuma1_d = DIR_UP
    elif kuma1_d == DIR_LEFT:
        if check_wall(kuma1_x, kuma1_y, kuma1_d, speed) == False:
            kuma1_x = kuma1_x - speed
        else:
            kuma1_d = DIR_RIGHT
    elif kuma1_d == DIR_RIGHT:
        if check_wall(kuma1_x, kuma1_y, kuma1_d, speed) == False:
            kuma1_x = kuma1_x + speed
        else:
            kuma1_d = DIR_LEFT
    kuma1_a = ANIMATION[tmr % 4]
    if abs(kuma1_x - pen_x) <= 40 and abs(kuma1_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy5():
    global mario_x, mario_y, mario_d, mario_a, idx, tmr
    speed = 15
    if mario_sd == -1:
        return
    elif mario_d == DIR_LEFT:
        if check_wall(mario_x, mario_y, mario_d, speed) == False:
            mario_x = mario_x - speed
        else:
            mario_d = DIR_RIGHT
    elif mario_d == DIR_RIGHT:
        if check_wall(mario_x, mario_y, mario_d, speed) == False:
            mario_x = mario_x + speed
        else:
            mario_d = DIR_LEFT
    mario_a = mario_d * 3 + ANIMATION[tmr % 4]#
    if abs(mario_x - pen_x) <= 40 and abs(mario_y - pen_y) <= 40:
        idx = 2
        tmr = 0

       
def main():
    global key, koff, tmr,  stage, idx, score, nokori
    tmr = tmr + 1
    draw_screen()
    if idx == 0:
        canvas.create_image(680,400, image=img_title, tag="SCREEN")
        if tmr % 10 < 5:
            draw_txt("Press SPACE !", 680, 550, 30, "yellow")
        if key == "space":
            stage = 1
            score = 0
            nokori = 3
            set_stage()
            set_chara_pos()
            idx = 1
           
    if idx == 1:
        move_penpen()
        move_enemy()
        move_enemy2()
        move_enemy3()
        move_enemy4()
        move_enemy5()
        if candy == 0:
            idx = 4
            tmr = 0
           
    if idx == 2:
        draw_txt("MISS", 680, 500, 60, "orange")
        if tmr == 1:
            nokori = nokori - 1
        if tmr == 30:
            if nokori == 0:
                idx = 3
                tmr = 0
            else:
                set_chara_pos()
                idx = 1
               
    if idx == 3:
        draw_txt("GAME OVER", 700, 500, 80, "red")
        if tmr == 50:
            idx = 0
           
    if idx == 4:
        if stage < 3:
            draw_txt("STAGE CLEAR", 680, 550, 40, "pink")
        else:
            draw_txt("ALL STAGE CLEAR", 680, 550, 40, "violet")
        if tmr == 30:
            if stage < 3:
                stage = stage + 1
                set_stage()
                set_chara_pos()
                idx = 1
            else:
                idx = 5
    if idx == 5:
        if tmr < 60:
            xr = 8 * tmr
            yr = 6 * tmr
            canvas.create_oval(720 - xr, 540 - yr, 720 + xr, 540 + yr, fill = "black",tag = "SCREEN")
        else:
            canvas.create_rectangle(0, 0, 1440, 1080, fill="black", tag = "SCREEN")
            canvas.create_image(720, 600, image=img_ending, tag = "SCREEN")
            draw_txt("Congratulations!", 720, 320, 80, BLINK[tmr % 6])
        if tmr == 300:
            idx = 0

    if koff == True:
        key = ""
        koff = False
               
    root.after(50,main)        
root = tkinter.Tk()

img_bg = [
    tkinter.PhotoImage(file="image_penpen/벽.png"),
    tkinter.PhotoImage(file="image_penpen/벽.png"),
    tkinter.PhotoImage(file="image_penpen/바닥.png"),
    tkinter.PhotoImage(file="image_penpen/다이아바닥.png")
]
img_pen = [
    tkinter.PhotoImage(file="image_penpen/금발00.png"),
    tkinter.PhotoImage(file="image_penpen/금발01.png"),
    tkinter.PhotoImage(file="image_penpen/금발02.png"),
    tkinter.PhotoImage(file="image_penpen/금발03.png"),
    tkinter.PhotoImage(file="image_penpen/금발04.png"),
    tkinter.PhotoImage(file="image_penpen/금발05.png"),
    tkinter.PhotoImage(file="image_penpen/금발06.png"),
    tkinter.PhotoImage(file="image_penpen/금발07.png"),
    tkinter.PhotoImage(file="image_penpen/금발08.png"),
    tkinter.PhotoImage(file="image_penpen/금발09.png"),
    tkinter.PhotoImage(file="image_penpen/금발10.png"),
    tkinter.PhotoImage(file="image_penpen/금발11.png"),
    tkinter.PhotoImage(file="image_penpen/hp1 (1).png")
]
img_red = [
    tkinter.PhotoImage(file="image_penpen/skeleton00.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton01.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton02.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton03.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton04.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton05.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton06.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton07.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton08.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton09.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton10.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton11.png")
]
img_red1 = [
    tkinter.PhotoImage(file="image_penpen/skeleton00.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton01.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton02.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton03.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton04.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton05.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton06.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton07.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton08.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton09.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton10.png"),
    tkinter.PhotoImage(file="image_penpen/skeleton11.png")
]
   
img_kuma = [
    tkinter.PhotoImage(file="image_penpen/팩맨왼.png"),
    tkinter.PhotoImage(file="image_penpen/팩맨오.png"),
    tkinter.PhotoImage(file="image_penpen/팩맨위.png"),
    #tkinter.PhotoImage(file="image_penpen/팩맨밑.png")
]

img_kuma1 = [
    tkinter.PhotoImage(file="image_penpen/팩맨왼.png"),
    tkinter.PhotoImage(file="image_penpen/팩맨오.png"),
    #tkinter.PhotoImage(file="image_penpen/팩맨위.png"),
    tkinter.PhotoImage(file="image_penpen/팩맨밑.png")
]
img_mario = [
    tkinter.PhotoImage(file="image_penpen/소닉00.png"),
    tkinter.PhotoImage(file="image_penpen/소닉01.png"),
    tkinter.PhotoImage(file="image_penpen/소닉02.png"),
    tkinter.PhotoImage(file="image_penpen/소닉03.png"),
    tkinter.PhotoImage(file="image_penpen/소닉04.png"),
    tkinter.PhotoImage(file="image_penpen/소닉05.png"),
    tkinter.PhotoImage(file="image_penpen/소닉06.png"),
    tkinter.PhotoImage(file="image_penpen/소닉07.png"),
    tkinter.PhotoImage(file="image_penpen/소닉08.png"),
    tkinter.PhotoImage(file="image_penpen/소닉09.png"),
    tkinter.PhotoImage(file="image_penpen/소닉10.png"),
    tkinter.PhotoImage(file="image_penpen/소닉11.png")
]

img_title = tkinter.PhotoImage(file="image_penpen/title.png")

img_ending = tkinter.PhotoImage(file="image_penpen/ending.png")

root.title("아슬아슬 펭귄 미로")
root.resizable(False,False)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas=tkinter.Canvas(width= 1440, height=1080)
canvas.pack()
set_stage()
set_chara_pos()
main()
root.mainloop()
