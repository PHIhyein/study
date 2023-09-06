

#문제
'''
for a in range(2, 9):
    print(a + "단 시작)
    for b in range(2, 9):
        print(a + "X" + b + "=" + a * b)
'''

#1. a, b가 끝나는 부분이 9이다(10이어야 한다)
#2. b가 2로 시작한다(1이어야 한다)
#3. print 부분의 타입이 다르다(a와 b는 int형이므로 str형으로 고쳐야 한다)
#혹은 print를 쉼표(,)로 구분한다

#해결
for a in range(2, 10):
    print(str(a) + "단 시작")
    for b in range(1, 10):
        print(a, "X", b, "=", a * b)



































'''
b = int(input("외우고 싶은 단 수: "))
for a in range(9):
    print(b * (a + 1))
'''

'''
print("7단을 외워보자.")
for a in range(1, 10):
    print(7 * a)

#

print("7단을 외워보자.")
for a in range(9):
    print(7 * (a + 1))
'''

'''
for a in range(2, 10):
    for b in range(1, 10):
        print(a, "x", b, "=", a * b)
    print("\n")
'''






