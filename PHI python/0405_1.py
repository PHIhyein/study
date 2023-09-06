import turtle as t
t.speed(0)


p = ["red", "hotpink", "pink", "beige"]
b = ["cyan", "skyblue", "blue", "darkblue"]

def draw(a):
    for x in range(len(a)):
        t.color(a[x])
        size = (x + 1) * 50
        for y in range(6):
            t.circle(size)
            t.right(60)


while 1:
    a = int(input("choice color \n1: pink \n2: blue\n"))

    if a == 1:
        draw(p)
    elif a == 2:
        draw(b)
    else:
         print("")

    print("")
