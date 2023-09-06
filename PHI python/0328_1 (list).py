
listrange = list(range(10))
print(listrange)
#0 ~ 9


listrange = list(range(1, 21, 5))
for i in listrange:
    print(i)
#1, 6, 11, 16


b = "파이썬은 아주 유용한 프로그래밍 언어입니다."
print(b[0:4])
print(b[0:3])
#시작값부터 끝난는 값 -1까지
print(b[:6])
#처음부터 5까지
print(b[6:])
#6부터 끝까지
print(b[:])
#전체
print(b[1:-1])
#뒤에서부터 n칸 뺀 것까지
