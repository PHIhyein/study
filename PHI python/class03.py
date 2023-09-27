class Gladiator:
    lv = 1
    hp = 100 + (lv * 20)
    mp = 35 + (lv * 5)
    pa = 77 + (lv * 7)
    ma = 23 + (lv * 1)
    pd = 50 + (lv * 3)
    md = 18 + (lv * 0.5)

    def __init__(self):
        self.name = "123456789"
        while (len(self.name) >= 9):
            self.name = input("이름 입력: ")
        print(self.name + "검투사님 환영합니다.\n")

    def lv_up(self):
        self.lv += 1
        print(str(self.lv) + "레벨이 되었습니다.\n")
        self.hp = 100 + (self.lv * 20)
        self.mp = 35 + (self.lv * 5)
        self.pa = 77 + (self.lv * 7)
        self.ma = 23 + (self.lv * 1)
        self.pd = 50 + (self.lv * 3)
        self.md = 18 + (self.lv * 0.5)
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n")

#

class Wizard:
    lv = 1
    hp = 90 + (lv * 10)
    mp = 70 + (lv * 15)
    pa = 23 + (lv * 1)
    ma = 77 + (lv * 7)
    pd = 18 + (lv * 0.5)
    md = 50 + (lv * 3)

    def __init__(self):
        self.name = "123456789"
        while (len(self.name) >= 9):
            self.name = input("이름 입력(9자 이내): ")
        print(self.name + "마법사님 환영합니다.\n")

    def lv_up(self):
        self.lv += 1
        print(self.lv, "레벨이 되었습니다\n")
        self.hp = 90 + (self.lv * 10)
        self.mp = 70 + (self.lv * 15)
        self.pa = 23 + (self.lv * 1)
        self.ma = 77 + (self.lv * 7)
        self.pd = 18 + (self.lv * 0.5)
        self.md = 50 + (self.lv * 3)
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n")











#print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n")

