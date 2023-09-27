class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name    #a = HousePark(init 내 변수)
    def travel(self, where):
        print("%s, %s 여행을 가다" %(self.fullname, where))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가다" %(self.fullname, where, day))


