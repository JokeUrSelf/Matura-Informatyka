file = [x.strip().split() for x in open("dane/pary.txt").readlines()]
# file = [x.strip().split() for x in open("dane/przyklad.txt").readlines()]

liczby = [int(x[0]) for x in file]
text = [x[1] for x in file]


def zadanie4_1():
    from math import sqrt
    def is_primary(n):
        if n < 2: return False
        for x in (2, int(sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True

    arr = []

    for x in liczby:
        if x % 2 == 0:
            tmp_arr = []
            for y in range(x // 2, x + 1):
                if is_primary(y) and is_primary(x - y):
                    if not tmp_arr or y - (x - y) > tmp_arr[1] - tmp_arr[2]:
                        tmp_arr = [x, y, x - y]
            arr.append(list(reversed(sorted(tmp_arr))))
    print("Zadanie 4.1:")
    for x in arr:
        print(f"{x}".strip("[]").replace(",", ""))
    return arr


def zadanie4_2():
    print("Zadanie 4.2:")
    for s in text:
        dic = {}
        for x in s:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        max_string = ""
        for k, v in dic.items():
            if len(max_string) < v:
                max_string = k * v
        print(max_string, len(max_string))


def zadanie4_3():
    print("Zadanie 4.3:")
    arr = [x[1] for x in file if int(x[0]) == len(x[1])]
    min_string = "z" * 60
    for x in arr:
        if len(x) <= len(min_string):
            if len(x) == len(min_string):
                for i, y in enumerate(x):
                    if ord(y) < ord(min_string[i]):
                        break
                    elif ord(y) > ord(min_string[i]):
                        x = min_string
                        break
            min_string = x
    print(len(min_string), min_string)


zadanie4_1()
zadanie4_2()
zadanie4_3()
