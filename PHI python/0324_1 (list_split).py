
listt = [11, 22, 33]
for i in range(len(listt)): #range는 0부터 값-1까지
    print(listt[i])


a, b = input("문자열 2개 입력: ").split()
#공백 기준으로 분리, int는 안됨, 엔터 안됨
#split괄호 안에 써놓은 기준은 길이를 셀 때 어느쪽에도 포함 안되고 제거됨
#C언어 scan을 split괄호 안의 것으로 구분하는 느낌?
print(a + "\n" + b)

c, d = map(int, input("숫자 2개 입력: ").split())
#map으로 입력받은 것의 형태 일괄변환
#int(input().split())는 안됨
#map 쉼표 첫 번째 형태 것으로, 쉼표 두 번째 것을 전부 형태 변환)
print(c, d, c + d)

                #--------------#map할 데이터 넣는 위치 (쉼표 이후 전부)
e, f = map(int, "10 20".split())
print(e, f, e + f)

g, h = input("'_'로 구분해보기: ").split('_') #ex)hi hello_hello hi
#split괄호 안에 분리 기준 넣기, 문자면 ''사이에 넣기
print(g + "\n" + h)


