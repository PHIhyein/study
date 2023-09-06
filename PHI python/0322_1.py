
x = 0

while x < 10:
    print('a')
    print('b')
    print('c')
    x += 1
    continue
    print('d')






























'''
milk = 0
cookie = 0
coffee = 0
coffee_non = 0


order = 0
price = 0

while 1:#\/\n -> 코드 이어쓰기
    order = int(input("주문할 물품범호를 입력하세요.\
\n1번 우유 500원 \n2번 쿠키 700원 \n3번 아메리카노 900원 \n4번 주문 끝내기\n"))


    if order == 1:
        print("\n우유 1개 추가\n")
        price += 500
        milk += 1
        

    elif order == 2:
        print("\n쿠키 1개 추가\n")
        price += 700
        cookie += 1


    elif order == 3:
        print("\n아메리카노 1개 추가\n")
        price += 900

        while 1:
            ask = input("디카페인을 원하시면 1을 입력하세요.")

            if ask == "1":
                print("디카페인을 드리겠습니다.\n")
                coffee_non += 1
                break
            
            else:
                coffee += 1
                break
        

    elif order == 4:
        print("\n영수증\n-----\n")
        if milk > 0:
            print("우유:", str(milk) + "개")
        if cookie > 0:
            print("쿠키:", str(cookie) + "개")
        if coffee_non > 0:
            print("아메리카노(디카페인):", str(coffee_non) + "개")
        if coffee > 0:
            print("아메리카노:", str(coffee) + "개")
        print("\n-----")
        print("결재 금액:", price)
        break


    else:
        print("잘못된 입력입니다.")




print("\n결재해주십시오.")
'''
