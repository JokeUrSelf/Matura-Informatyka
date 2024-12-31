# file = [x.strip("\n") for x in open("dane/przyklad.txt").readlines()]
file = [x.strip("\n") for x in open("dane/sygnaly.txt").readlines()]

def zadanie4_1():
    for i in range(39, len(file), 40):
        try:
            print(file[i][9], end="")
        except IndexError: pass
def zadanie4_2():
    maxi = ["",0]
    for x in file:
        if maxi[1] < len(set(x)):
            maxi[0] = ""
            for y in x:
                if y not in maxi[0]:
                    maxi[0]+=y
            maxi[1] = len(set(x))
    print(maxi[0], maxi[1])
def zadanie4_3():
    for x in file:
        tmp = True
        for i in range(0, len(x)-1):
            if not abs(ord(x[i]) - ord(x[i+1])) <= 10:
                tmp = False
                break
        if tmp: print(x)


# zadanie4_1()
# zadanie4_2()
zadanie4_3()
