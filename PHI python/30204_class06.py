class Gladiator:
    lv = 0
    full = [100, 35, 77, 23, 50, 18]
    up = [20, 5, 7, 1, 3, 0.5]
    now = [100, 35, 77, 23, 50, 18]

    job = "검투사"

    def __init__(self):
        self.name = ""
        while (len(self.name) > 9 or self.name == ""):
            self.name = input("이름을 입력하세요(1~9글자): ")
        print(self.name , self.job + "님 환영합니다.\n")
        self.lv_up()

    def lv_up(self):
        self.lv += 1
        print(str(self.lv) + "레벨이 되었습니다.\n")
        for x in range(len(self.full)):
            self.full[x] += self.up[x]
            self.now[x] = self.full[x]
            print(self.full[x])

    def __add__(self, a):   #hp_up
        heal = ((self.full[0] / 100) * a)
        if (self.now[0] + heal > self.full[0]):
            heal = self.full[0] - self.now[0]
            a = round(heal * (100 / self.full[0]), 2)
            self.now[0] = self.full[0]
        else:
            self.now[0] += heal
        print("hp가 " + str(a) + "% 상승했습니다. \n현재 hp:", self.now[0], "\n")

    def __sub__(self, a):   #hp_down
        self.now[0] -= a
        if self.now[0] <= 0:
            print("캐릭터가 더 이상 탐험할 수 없습니다.\n")
            self.now[0] = 0
        else:
            print("hp가 " + str(a) + "만큼 감소했습니다. \n현재 hp:", self.now[0], "\n")


#


class Wizard(Gladiator):
    job = "마법사"

    full = [90, 70, 23, 77, 18, 50]
    up = [10, 15, 1, 7, 0.5, 3]
    now = [90, 70, 23, 77, 18, 50]


