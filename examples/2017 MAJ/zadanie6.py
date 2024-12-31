file = [x.strip("\n").split(" ") for x in open("dane/dane.txt").readlines()]
# file = [x.strip("\n").split(" ") for x in open("dane/przyklad.txt").readlines()]

for i, x in enumerate(file):
    for j, y in enumerate(x):
        file[i][j] = int(y)

def zadanie6_1():
    mini = file[0][0]
    maxi = file[0][0]
    for x in file:
        for y in x:
            mini = min(mini,y)
            maxi = max(maxi,y)
    print("Najciemniejszy:", mini)
    print("Najasniejszy:", maxi)

def zadanie6_2():
    counter = 0
    for x in file:
        if x != x[::-1]:
            counter+=1
    print(counter)

def zadanie6_3():
    arr = [[0 for _ in range(320)] for _ in range(200)]

    for y in range(len(file)):
        for x in range(len(file[0])):

            def ch(_y, _x):
                if file[0] < _x < 0 or _y < 0: return False
                try:return abs(file[_y][_x]-file[y][x]) > 128
                except IndexError: return False

            if True in {ch(y+1,x),
                        ch(y-1,x),
                        ch(y,x+1),
                        ch(y,x-1)
                        }: arr[y][x] = 1
    counter = 0
    for x in arr:
        counter+=sum(x)
    print(counter)

def zadanie6_4():
    maxi = 0
    for x in range(320):
        counter = 1
        for y in range(200):
            try: bl = file[y][x] == file[y+1][x]
            except IndexError: bl = file[y][x] == file[y-1][x]
            if bl: counter+=1
            else:
                maxi = max(maxi, counter)
                counter = 1
        maxi = max(maxi, counter)
    print(maxi)


# zadanie6_1()
# zadanie6_2()
# zadanie6_3()
zadanie6_4()