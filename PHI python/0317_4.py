a = int(input("음식 배달 시키려면 1, 아니면 0을 입력: "))

if a == 1:
    b = input("원하는 메뉴 고르기 \n1번 중식 \n2번 양식 \n다른 음식\n")


    if b == "1번" or b == "중식" or b == "1":
        c = input("1번 짜장 \n2번 짬뽕\n")
        
        if c =="1번" or c == "짜장" or c == "1":
            print("짜장 먹자!")
            
        elif c == "2번" or c == "짬뽕" or c == "2":
            print("짬뽕 먹자!")


    elif b == "2번" or b == "양식" or b == "2":
        c = input("1번 파스타 \n2번 스테이크\n")
        
        if c =="1번" or c == "파스타" or c == "1":
            print("파스타 먹자")
            
        elif c == "2번" or c == "스테이크" or c == "2":
            print("스테이크 먹자")

    else:
        print("네가 찾아보렴")


elif a == 0:
    pass


else:
    print("1 또는 0으로 입력해주세요.")

'''
샤랄라
'''
