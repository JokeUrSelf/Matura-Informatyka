# file = [int(x.strip("\n")) for x in open("dane\przyklad.txt").readlines()]
file = [int(x.strip("\n")) for x in open("dane\liczby.txt").readlines()]

def zadanie4_1():
    counter = 0
    for x in file:
        while x > 1: x/=3
        counter+=int(x)
    print(counter)
def zadanie4_2():
    def factorial(f):
        if f <= 1:
            return 1
        return factorial(f-1) * f
    for x in file:
        sum = 0
        n = x
        while n > 0:
            sum += factorial(n%10)
            n//=10
        if sum == x:
            print(x)
def zadanie4_3():
    def NWD(x, y):
        if x < y: x,y=y,x
        if x%y == 0: return y
        return NWD(y,x%y)
    max_arr = []
    arr = []
    final_NWD = 1
    curr_NWD = 1
    for x in file:
        if not arr: curr_NWD = x
        curr_NWD = NWD(curr_NWD, x)
        if curr_NWD > 1:
            arr.append(x)
        else:
            if len(max_arr) < len(arr):
                max_arr = arr
                final_NWD = curr_NWD
            arr = []
    print(max_arr[0], len(max_arr), final_NWD)

# zadanie4_1()
# zadanie4_2()
# zadanie4_3()
