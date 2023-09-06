'''
tutu = tuple(range(10, 20, 2))
print(tutu)
#튜플의 값은 변경, 추가 불가
tutu = 10, 20
print(tutu)
print(type(tutu))
#같은 이름으로 재선언은 가능
#튜플은 콤마로 구분
#괄호로 묶지 않아도 됨
len(tutu)
#len도 사용 가능
'''



b = [100, 200, 300, 400, 500, 600]

c = list(range(0, 6, 2))#인덱스용 리스트

for x in c:
    print(b[x])

































