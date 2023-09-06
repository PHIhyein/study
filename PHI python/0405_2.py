from random import randint


rolling = 'y'

while (rolling == 'y'):
    print("주사위가 굴러갑니다.\n")
    a, b, c = randint(1, 7), randint(1, 7), randint(1, 7)

    print("1번 주사위:", a)
    print("2번 주사위:", b)
    print("3번 주사위:", c)

    if a == b and b == c:
        if a == 7:
            print("잭팟!")
        else:
            print("트리플!")

    if a == b + 1 and b == c + 1 or a == b - 1 and b == c - 1:
        print("스트레이트")
    
    rolling = input("한 번 더 굴리려면 'y'를, 종료하려면 'n'을 입력하시요.")

print("주사위 프로그램이 종료됩니다.")

