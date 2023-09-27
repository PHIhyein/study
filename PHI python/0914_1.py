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
        self.hp += 20
        self.mp += 5
        self.pa += 7
        self.ma += 1
        self.pd += 3
        self.md += 0.5
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n")

    def hp_up(self, a):
        print("HP가", a, "상승했습니다.\n")
        print("hp: "+str(self.hp)+"\nmp: "+str(self.mp)+"\npa: "+str(self.pa)+"\nma: "+str(self.ma)+"\npd: "+str(self.pd)+"\nmd: "+str(self.md)+"\n")
        return self.hp + a    #g1.hp = g1.hp_up(hp_item(인수))로 실행

g = Gladiator()
g.lv_up()
g.hp_up(10)
g.lv_up()
g.hp_up(10)
g.lv_up()
g.hp_up(10)
g.lv_up()
g.hp_up(10)
g.lv_up()
g.hp_up(10)

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



#인스턴스명.매소드(인수) = 클래스명.매소드(인스턴스명, 인수) 으로 사용 가능


        




















#####



'''#
class Calculator:   #보통 첫 문자는 대문자로 시작
    def __init__(self): #기본 설정/초기화
        self.result = 0   #메서드의 첫 번째 매개변수는 반드시 self로 지정(넣기만 하고 무시해도 됨)
                            #self 는 인스턴스
    def add(self, num):
        self.result += num
        return self.result

    def minus(self, num):
        self.result -= num
        return self.result

    def mul(self, num1, num2):
        self.result = num1 * num2
        return self.result


cal1 = Calculator() #인스턴스 생성
cal2 = Calculator()
cal3 = Calculator()



print(cal1.add(3))  #매소드 호출
print(cal1.minus(4))
print(cal2.add(3))
print(cal2.minus(7))


print(cal3.mul(2, 4))
'''

