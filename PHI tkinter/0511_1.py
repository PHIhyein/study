import tkinter #배경 생성 및 이동

x = 480
def scroll_bg():
    global x #전역변수 가져옴
    
    x = x - 1 #.after의 초마다 x값 감소시키다가 0이 되면 값 초기화
    if x == 0:
        x = 480
        
    canvas.delete("BG") #캔버스 지우고, x값에 화면 넓이의 반을 뺀 것과 더한 위치에 배경 생성
    canvas.create_image(x - 240, 150, image = img_bg, tag = "BG")
    canvas.create_image(x + 240, 150, image = img_bg, tag = "BG")
    
    root.after(25, scroll_bg)

root = tkinter.Tk()
root.title("배경 스크롤")
canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file = "park.png")
scroll_bg()

root.mainloop()



















'''
root = tkinter.Tk()
root.title("배경")

canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
canvas.create_image(240, 150, image = img_bg)

root.mainloop()
'''






'''
import datetime

def time_now():
    d = datetime.datetime.now()
    t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second)
    label["text"] = t
    root.after(1000, time_now)

root = tkinter.Tk()
root.geometry("400x100")
root.title("간이 계산")
label = tkinter.Label(font=("돋움", 60))
label.pack()
time_now()
root.mainloop()
'''





'''
def key_down(e):
    key_c = e.keycode
    label1["text"] = "keycode " + str(key_c)
    key_s = e.keysym
    label2["text"] = "keysym " + key_s


root = tkinter.Tk()
root.geometry("400x200")
root.title("파이썬 GUI")

root.bind("<KeyPress>", key_down)
label1 = tkinter.Label(text="keycode", font=("궁서", 20))
label1.place(x=0, y=0)
label2 = tkinter.Label(text="keysym", font=("궁서", 20))
label2.place(x=0, y=80)

root.mainloop()
'''
