
def plus(*a):
    c = 0
    for x in a:
        c = c + x
    print(c)
    

def mul(*a):
    c = 1
    for x in a:
        c = c * x
    print(c)


def avg(*a):
    c = 0
    b = 0
    for x in a:
        c = c + x
        b = b + 1
    print(c / b)















def scan():
    x = int(input())
    return x

