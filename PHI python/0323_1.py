
pw = "0000" #비번
ipw = "0000" #초기화


while True:
    i = input("1번 문 열기, 2번 비밀번호 변경 ")


    if i == "1":
        ipw = input("비밀번호 입력: ")

        if ipw == pw:
            print("문이 열립니다.")

        else:
            print("비밀번호가 틀렸습니다.")


    elif i == "2":
        ipw = input("현재 비밀번호 입력: ")
        
        if ipw == pw:
            print("비밀번호는 4자 이상 8자 이하로 설정할 수 있습니다.")
            npw = input("새 비밀번호 입력: ")

            if len(npw) >= 4 and len(npw) <= 8:
                npw2 = input("새 비밀번호 재입력: ")

                if npw == npw2:
                    pw = npw
                    print("비밀번호 변경 완료")


                else:
                    print("새 비밀번호가 다르게 입력됐습니다.")


            else:
                print("4자 이상 8자 이하가 아닙니다.")
                

        else:
            print("비밀번호가 틀렸습니다.")


    else:
        pass




































'''


pw = "0000" #비번
ipw = "0000" #입력 비번


#문열기
while 1:
    i = input("1번 문 열기 \n2번 비밀번호 변경 \n") #문열기와 비번 변경 중 선택


    if i == "1": #문 열기
        ipw = input("비밀번호 입력: ")

        if ipw == pw: #비번 일치
            print("문이 열립니다.\n")

        else: #비번 불일
            print("비밀번호가 틀렸습니다.\n")


    elif i == "2": #비번 번경
        ipw = input("\n현재 비밀번호 입력: ")

        
        if ipw == pw: #현재 비번과 일치
            print("\n비밀번호는 4자 이상 8자 이하로 설정할 수 있습니다.")
            npw = input("새 비밀번호 입력: ")

            if len(npw) >= 4 and len(npw) <= 8: #새 비번 글자 수가 4자 이상 8자 이하면 새 비번 재입력 받기
                npw2 = input("새 비밀번호 재입력: ")
                
                if npw == npw2: #두 번 입력한 새 비번 일치
                    pw = npw #새 비번으로 바뀜
                    print("비밀번호 변경 완료\n")

                else: #두 번 입력한 새 비번이 불일치
                    print("새 비밀번호가 다르게 입력됐습니다.\n")


            else: #새 비번 글자수가 조건 충족 못 함
                print("4자 이상 8자 이하가 아닙니다.\n")

                
        else: #현재 비번과 일치하지 않음
            print("비밀번호가 틀렸습니다.\n")


    else: #문열기도 비번 변경도 아님
        pass


'''

