'''
a = [1, 2]
a.append(3)#(요소)
print(a)
#list 가장 뒤에 값 추가하기


b = [10, 20, 30]
print(b)
tt.extend(b)#(리스트)
print(a)
#list 뒤에 다른 list 붙이기


'''
'''
a.append(b)#(요소)
print(a)
#list 통째로 리스트 상태 그대로 붙임
'''

'''


a.insert(3, 100)#(원하는 위치 인덱스, 넣을 값)
print(a)
#원하는 위치에 요소 추가


a.remove(100)#삭제할 특정 값(칸 아님)
print(a)
#list의 특정 값 삭제하기


a.pop()
print(a)
#list의 마지막 값 삭제


a.index(10)#(인덱스 찾을 값)
#특정 값의 인덱스(위치) 구하기


a.extend(a)
a.count(10)#(특정 값)
#list에서 특정 값의 개수 구하기


a.reverse()
#순서를 반대로 바꿈


a.sort()
#오름차순 정렬
a.sort(reverse=True)
#내림차순 정렬


b.clear()
print(b)
#모든 값 삭제


del a[2]
#인덱스 칸에 들어있는 것 삭제
a.pop(1)
#인덱스 값 제외하고 전체 삭제
'''







a = ["good", "love", "bravo", "cute", "error", "best"]

a.remove("error")
a.sort()

print(a)





















































