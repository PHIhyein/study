class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name    #a = HousePark(init 내 변수)
    def travel(self, where):
        print("%s, %s 여행을 가다" %(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네." %(self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s, 싸우네." %(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼!" %(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼!" %(self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가다" %(self.fullname, where, day))











#선언하면 실행 가능한 함수 : 메소드
#클래스명, 연산자, 매개변수
#r:reverse (ex:__radd__)
#over - 덮어쓰기 -> 연산자 오버로딩
#add : +기호 -> __add__ : 호출 시 +기호 사용
#매개변수 1개를 받는 함수를 쉽게 호출하기 위해 연산자 기호를 사용할 뿐

