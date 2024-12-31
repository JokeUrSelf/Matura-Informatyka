file = [x.strip("\n") for x in open("dane/punkty.txt").readlines()]
xs = [int(x.split(" ")[0]) for x in file]
ys = [int(y.split(" ")[1]) for y in file]

def primary_num(n):
    from math import sqrt
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def zadanie4_1():
    counter = 0
    for i in range(len(file)):
        if primary_num(xs[i]) and primary_num(ys[i]):
            counter+=1
    print(counter)

def zadanie4_2():
    def result_set(n):
        sett = set()
        while n > 0:
            sett.add(n%10)
            n//=10
        return sett
    counter = 0
    for i in range(len(file)):
        if result_set(xs[i]) == result_set(ys[i]):
            counter+=1
    print(counter)

def zadanie4_3():
    import math as m
    max_arr = [0]
    for i in range(len(file)):
        for j in range(len(file)):
            d = m.sqrt(m.pow(xs[i] - xs[j],2) + m.pow(ys[i] - ys[j],2))
            if d > max_arr[0]:
                max_arr = [d, xs[i], ys[i], xs[j], ys[j]]

    print("Długość:", int(max_arr[0]))
    print("Wspolrzedne A:", max_arr[1], max_arr[2])
    print("Wspolrzedne B:", max_arr[3], max_arr[4])

def zadanie4_4():
    equal = 0
    less = 0
    more = 0
    for i in range(len(file)):
        if (abs(xs[i]) == 5000 and abs(ys[i]) <= 5000) or (abs(ys[i]) == 5000 and abs(xs[i]) <= 5000):
            equal+=1
        elif abs(xs[i]) < 5000 and abs(ys[i]) < 5000:
            less +=1
        elif abs(xs[i]) > 5000 or abs(ys[i]):
            more +=1
    print("Na przedziale", equal)
    print("W przedzialach", less)
    print("Za przedzialem", more)
# zadanie4_1()
# zadanie4_2()
# zadanie4_3()
zadanie4_4()
