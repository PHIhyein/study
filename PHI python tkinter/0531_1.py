import tkinter

def mouse_click(e):
    px = e.x
    py = e.y
    print("마우스 포인터 좌표:({},{})".format(px,py))
    
    mx = int(px/48)
    my = int(py/48)
    if 0 <= mx <= 6 and 0 <= my <= 4:
        n = map_data[my][mx]
        print("여기에 있는 맵 칩은 " + CHIP_NAME[n])
        print("")

root = tkinter.Tk()
root.title("맵 데이터")
canvas = tkinter.Canvas(width = 336, height = 192)
canvas.pack()

canvas.bind("<Button>", mouse_click)
CHIP_NAME = ["풀", "꽃", "숲", "바다"]
                                     
img = [
    tkinter.PhotoImage(file = "chip0.png"),
    tkinter.PhotoImage(file = "chip1.png"),
    tkinter.PhotoImage(file = "chip2.png"),
    tkinter.PhotoImage(file = "chip3.png")
    ]
map_data = [
    [0, 1, 0, 2, 2, 2, 2],
    [3, 0, 0, 0, 2, 2, 2],
    [3, 0, 0, 1, 0, 0, 0],
    [3, 3, 3, 3, 0, 0, 0]
    ]

for y in range(4):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x * 48 + 24, y * 48 + 24, image = img[n])
root.mainloop()










'''
x = 0
ani = 0

def animation():
    global x, ani
    x += 4
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x - 240, 150, image = img_bg, tag = "BG")
    canvas.create_image(x + 240, 150, image = img_bg, tag = "BG")
    ani = (ani + 1) % 4
    canvas.create_image(240, 200, image = img_dog[ani], tag = "BG")
    root.after(200, animation)

root = tkinter.Tk()
root.title("애니메이션")
canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file = "park.png")
img_dog = [
    tkinter.PhotoImage(file = "dog0.png"),
    tkinter.PhotoImage(file = "dog1.png"),
    tkinter.PhotoImage(file = "dog2.png"),
    tkinter.PhotoImage(file = "dog3.png"),
    ]
animation()
root.mainloop()
'''
