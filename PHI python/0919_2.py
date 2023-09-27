class mom:
    def __init__(self):
        print("mom 클래스를 생성합니다")
    def m1(self):
            print("키가 큽니다")

class dad:
    def __init__(self):
        print("dad 클래스를 생성합니다")
    def d1(self):
        print("성격이 느긋합니다")

class child(mom, dad):
    def __init__(self):
        print("child 클래스를 생성합니다")
    def c1(self):
        child.m1(self)
        child.d1(self)
        print("코딩을 좋아합니다")






