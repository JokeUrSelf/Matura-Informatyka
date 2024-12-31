# file = [x.strip() for x in open('dane/przyklad.txt').readlines()]
file = [x.strip() for x in open('dane/instrukcje.txt').readlines()]

def zadanie4_1():
    arr = []
    for x in file:
        ins = x[:-2]
        w = x[-1]
        if ins == 'DOPISZ':
            arr.append(w)
        elif ins == 'USUN':
            if arr: arr.pop()
    print(len(arr))


def zadanie4_2():
    amount = 0
    ins = 1
    maxi = last = [0, '']
    for x in file:
        current_ins = x[:-2]
        if current_ins != last[ins]:
            if maxi[amount] < last[amount]:
                maxi = last
            last = [1, current_ins]
        else:
            last[amount] += 1
    print(str(maxi).strip('[]'))


def zadanie4_3():
    dic = {}
    for x in file:
        ins = x[:-2]
        w = x[-1]
        if ins == 'DOPISZ':
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
    l = ''
    maxi = max(dic.values())
    for k in dic:
        if dic[k] == maxi:
            l = k
            break
    print(maxi, l)

def zadanie4_4():
    arr = []
    for x in file:
        ins = x[:-2]
        w = x[-1]
        if ins == 'DOPISZ':
            arr.append(w)
        elif ins == 'ZMIEN':
            arr[-1] = w
        elif ins == 'USUN':
            if arr: arr.pop()
        else:
            arr[arr.index(w)]=chr(ord(w) + 1) if w!='Z' else 'A'

    print("".join(arr))


# zadanie4_1()
# zadanie4_2()
# zadanie4_3()
zadanie4_4()
