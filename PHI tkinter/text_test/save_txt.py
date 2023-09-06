def save1():
    save = open("save.txt", "r", encoding='UTF8')
    information = save.readlines()
    save.close()

    name = input("이름: ") + "\n"
    number = input("번호(혹은 전화번호): ") + "\n"
    information.append(name)
    information.append(number)
    information.append("\n")

    save = open("save.txt", "w", encoding='UTF8')
    for wt in range(0, len(information)):
        save.write(information[wt])
    save.close()
    


def save():
    save = open("save.txt", "a", encoding='UTF8')
    name = input("이름: ") + "\n"
    number = input("번호(혹은 전화번호): ") + "\n"
    save.write(name)
    save.write(number)
    save.write("\n")
    save.close()


'''
save = open("save.txt", "a", encoding='UTF8')
name = input("이름: ") + "\n"
number = input("번호(혹은 전화번호): ") + "\n"
save.write(name)
save.write(number)
save.write("\n")
save.close()
'''



#line.strip() -> 막줄 내용이 공백이면 읽지 않는 듯(a, "\n"), 하지만 (a, "\n", b)면 \n도 취급함
#print("내용", end="") -> 무엇으로 끝낼지 end에 적음, 출력할 땐 띄어쓰기 없이 붙여서 출력

