w = int(input("보유 현금: "))

if w >= 10000:
    print("택시 타도 되겠다~")

elif w >= 5000:
    print("가까운 곳이면 택시 타자!")

elif w >= 1500:
    print("버스 타자~")

else:
    print("걸어가자")
