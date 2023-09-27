class Gladiator:
    lv = 1
    max_hp = 120
    hp = max_hp    #현재 체력은 최대체력
    mp = 40
    pa = 84
    ma = 24
    pd = 53
    md = 18.5

    job = "검투사"

    def __init__(self):
        self.name = ""
        while (len(self.name) > 9 or self.name == ""):
            self.name = input("이름을 입력하세요(1~9글자): ")
        print(self.name , self.job + "님 환영합니다.\n")

    def lv_up(self):
        self.lv += 1
        print(str(self.lv) + "레벨이 되었습니다.\n")
        self.max_hp += 20
        self.hp = self.max_hp   #현재 체력은 최대체력
        self.mp += 5
        self.pa += 7
        self.ma += 1
        self.pd += 3
        self.md += 0.5
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n\n")

    def __add__(self, a):   #hp_up
        self.hp += ((self.max_hp / 100) * a) #최대 체력의 a%만큼 체력 회복
        if (self.hp > self.max_hp):  #회복량이 최대체력을 넘김
            self.hp = self.max_hp    #최대체력을 못넘기게
        print("HP가 " + str(a) + "% 상승했습니다.\n")
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n\n")

#

class Wizard(Gladiator):
    job = "마법사"
#
    max_hp = 100
    hp = max_hp
    mp = 85
    pa = 24
    ma = 84
    pd = 18.5
    md = 53

    def lv_up(self):
        self.lv += 1
        print(str(self.lv) + "레벨이 되었습니다.\n")
        self.max_hp += 10
        self.hp = self.max_hp   #현재 체력은 최대체력
        self.mp += 15
        self.pa += 1
        self.ma += 7
        self.pd += 0.5
        self.md += 3
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n\n")

