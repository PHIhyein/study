'''
1. init에서 이름 한 글자 이상 입력
2. init에서 이름 9자 이하
3. 바르게 입력 까지 반복


4. hp_up에서 hp는 최대값을 넘을 수 없음
5. hp_up 매개변수 a를 숫자로 받고 현재 lv에서 가능한 hp 최대값의 a%만큼 증가시킨다

4-> 내가 가질 수 있는 레벨에서의 체력 최댓값

파일명 학번_class03

'''


class Gladiator:
    lv = 1
    max_hp = 120
    hp = max_hp    #현재 체력은 최대체력
    mp = 40
    pa = 84
    ma = 24
    pd = 53
    md = 18.5

    def __init__(self):
        self.name = ""
        while (len(self.name) > 9 or self.name == ""):
            self.name = input("이름을 입력하세요(1~9글자): ")
        print(self.name + "검투사님 환영합니다.\n")

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

    def hp_up(self, a):
        heal = ((self.max_hp / 100) * a)    #회복량
        if (self.hp + heal > self.max_hp):  #회복량이 최대체력을 넘김
            heal = self.max_hp - self.hp    #회복량 조정 (a% = 회복량 * (100 / 최대체력)), 현재체력은 항상 최대체력보다 작거나 같음(0~최대체력)
            a = round(heal * (100 / self.max_hp), 2) #회복량 표시(a%)를 알맞게 바꿈
            self.hp = self.max_hp    #최대체력을 못넘기게
        else:
            self.hp += heal #최대 체력의 a%만큼 체력 회복
        print("HP가 " + str(a) + "% 상승했습니다.\n")
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n\n")
