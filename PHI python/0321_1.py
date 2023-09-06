a = int(input("배달 1\n아니면 0\n"))

if a == 1:
    b = input("\n1번 중식\n2번 양식\n그 외 다른거\n")


    if  b == "1번" or b == "중식" or b == "1":
        c = input("\n1번 짜장\n2번 짬뽕\n")

        if c == "1번" or c == "짜장" or c == "1":
            print("짜장 먹자")

        elif c == "2번" or c == "짬뽕" or c == "2":
            print("짬뽕 먹자")
        
        
    elif b == "2번" or b == "양식" or b == "2":
        c = input("\n1번 스테이크\n2번 파스타\n")

        if c == "1번" or c == "스테이크" or c == "1":
            print("스테이크 먹자")

        elif c == "2번" or c == "파스타" or c == "2":
            print("파스타 먹자")


    else:
        print("네가 찾아보렴")
        


elif a == 0:
    pass

else:
    print("1 또는 0 으로 대답")


#저번에 했던거 복습
