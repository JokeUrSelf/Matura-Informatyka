if 0 and 'znajdz palindrom':
    isPalindrome = lambda head: head == head[::-1]
    print(isPalindrome([1, 2, 2, 1]))
    
if 0 and 'szybkie znależenie stopniu':
    def fast_pow(x: int, n: int):
        r = 1
        while n > 0:
            if n % 2 == 1: r *= x
            n //= 2
            x *= x
        return r

    print(fast_pow(2, 4))
    
if 0 and 'znajdz sumę cyfr w liczbie':
    def func(n):
        if n == 0: return 0
        return func(n // 10) + n % 10

    print(func(1234))
    
if 0 and 'liczba cyfr potrzebna do zapisania liczby dwojkowej':
    def bin_length(n):
        i = 0
        while n > 0:
            n //= 2
            i += 1
        return i

    print(bin_length(185))
    
if 0 and 'base-4 to base-2':
    def four_to_bin(n):
        r = 0
        i = 1
        while n > 0:
            r += (n % 10 // 2 * 10 + n % 10 % 2) * i
            i *= 100
            n //= 10
        return r

    print(four_to_bin(312))
    
if 0 and 'znajdż największą sumę podciągu (Kadanes algorithm)':
    def func(arr):
        r = 0
        maxi = arr[0]
        for x in arr:
            r += x
            r = max(r, x)
            maxi = max(r, maxi)
        return maxi

    print(func([1, 2, 3, 4, 5, 6]))
    
if 0 and 'największy wspolny prefiks':
    def longestCommonPrefix(strs) -> str:
        r = ""
        for i in range(len(strs[0])):
            x = ""
            for x in strs:
                if i >= len(x) or x[i] != strs[0][i]:
                    return r
            r += x[i]
        return r

    print(longestCommonPrefix(["flower", "flow", "flight"]))
    
if 0 and 'czy jest to liczba perwsza':
    def isFirstNumber(num: int):
        from math import sqrt
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0:
                return False
        return True

    print(isFirstNumber(23456789))
    
if 0 and 'ile liczb pierwszych zawiera lista':
    def isFirstNumber(num: int):
        from math import sqrt
        if num % 2 == 0 and num != 2 or num < 2: return 0
        for x in range(3, int(sqrt(num)) + 1, 2):
            if num % x == 0 and num != x: return 0
        return 1


    def howManyFirstNumbers(list_of_numbers):
        sum = 0
        for num in list_of_numbers:
            sum += isFirstNumber(num)
        return sum

    print(howManyFirstNumbers(list(range(1067834))))
    
if 0 and 'pierwsza liczba parzysta (binarny poszuk)':
    def func(A):
        l, r = 0, len(A) - 1
        while r > l:
            m = (l + r) // 2
            if A[m] % 2 == 0:
                if A[m - 1] % 2 == 1:
                    return A[m]
                r = m
            else:
                l = m + 1
        return A[r]

    print(func([3, 4]))
    
if 0 and 'znajdż odpowiedność nawiasów optymizacja':
    def validate_braces_optimized(s):
        pair = {'}': '{', ']': '[', ')': '('}
        stack = []
        for i in s:
            try:
                if pair[i] != stack.pop(): return False
            except:
                stack.append(i)
        return not stack

    print(validate_braces_optimized("(()([]){})[]"))
    
if 0 and 'połąć dwie listy posortowane':
    def merge(list1, list2):
        l = min(len(list1), len(list2))
        arr = []
        while list1 and list2:
            if list1[0] <= list2[0]:
                arr.append(list1.pop(0))
            else:
                arr.append(list2.pop(0))
        list1.extend(list2)
        arr.extend(list1)
        return arr

    print(merge([1, 3, 4, 10], [1, 3, 5, 6, 34]))
    
if 0 and 'znajdż mediane posortowanej tablicy':
    def findMedianSortedArrays(arr) -> float:
        N = len(arr)
        x = (N - 1) // 2
        return arr[x] if N % 2 else (arr[x] + arr[x + 1]) / 2

    print(sorted([1, 12, 35, 123, 12, 5, 12, 5, 12]))
    
if 0 and "generacja siatki liczb pierwszych":
    def func(n):
        from math import sqrt
        def is_primary_number(n):
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0: return False
            return True

        grid = [x for x in range(3, n + 1, 2) if is_primary_number(x)]
        return [2] + grid

    print(func(1000000))
    
if 0 and 'pierwsza niepowtarzająca się litera':
    def firstNonRepeatingCharacter(s):
        if 0 and 'solution 1':
            for i in range(len(s)):
                if s[i] not in s[:i] + s[i + 1:]:
                    return s[i]
            return "_"

        if 1 and 'solution 2':
            dic = {k: 0 for k in s}
            for x in s:
                dic[x] += 1
            for x in s:
                if dic[x] == 1:
                    return x
            return '_'

    print(firstNonRepeatingCharacter(
        "abcbcvbnmzxcvbnmzxcvbnmzcvbnmzxcvbnmsdfaasfdasdfasdfasdfkad"
    ))
    
if 0 and 'znajdż indeksy dwoch elemntów, suma których jest równa znaczeniu zmiennej "target"':
    def twoSum(nums, target: int):
        dic = {}
        for i, x in enumerate(nums):
            if target - x in dic:
                return [dic[target - x], i]
            dic[x] = i
        return []

    print(twoSum([1, 2, 5, 6, 1, 3, 4, 2, 6, 1], 12))

if 0 and 'czy liczba jest wesoła':
    def is_number_funny(n):
        arr = []
        while True:
            arr.append(n)
            tmp = 0
            while n > 0:
                tmp += n % 10 * n % 10
                n //= 10
            if tmp == 1: return True
            if tmp in arr: return False
            n = tmp

    print(is_number_funny(7))
    
if 0 and 'znajdz indeksy trzech elementów, suma których daje zero':
    def twoSum(nums, target: int):
        dic = {}
        for i, x in enumerate(nums):
            if target - x in dic:
                return [dic[target - x], i]
            dic[x] = i
        return []


    def three_sum(nums):
        for i, x in enumerate(nums):
            smth = twoSum(nums, -x)
            if smth:
                return [i] + smth
        return []

    print(three_sum([1, 2, 3, -4]))
    
if 0 and 'najdłuższy ciąg niepowtarzających się literek':
    def longest_substring(s):
        maxi = 0
        suma = 1
        last_letter = s[0]
        for i, x in enumerate(s):
            if x != last_letter:
                suma += 1
            else:
                maxi = max(suma, maxi)
                suma = 1
            last_letter = x
        return maxi

    print(longest_substring("qhhhwerfffzz"))
    
if 0 and 'zamiana liczb miedzy systemami liczbowynmi':
    def charToNumber(val: chr) -> int:
        val = ord(val.upper())
        if val >= ord('A'): return val - 55
        if val <= ord('9'): return val - 48


    def numberToChar(val: int) -> chr:
        if val >= 10: return chr(val + 55)
        if val <= 9: return chr(val + 48)


    def convert(value, init_base: int, final_base: int):
        if init_base < 2 or final_base < 2: return -1

        result = 0
        n = 1
        result2 = ""

        for x in reversed(value):
            result += charToNumber(x) * n
            n *= init_base

        while result > 0:
            result2 = numberToChar(result % final_base) + result2
            result //= final_base
        return result2

    print(convert("17A1", 16, 2))

if 0 and 'silniowy system pozycyjny':
    def func(n):
        result = 0
        smth = 1
        i = 2
        while n > 0:
            result += n % i * smth
            smth *= 10
            n //= i
            i += 1
        return result

    print(func(3628799))
    
if 0 and 'ile dzielników ma liczba':
    def func(n):
        i = 0
        for x in range(1, n // 2 + 1):
            if n % x == 0: i += 1
        return i + 1


    print(func(23))
    
if 0 and 'sortowanie bąbelkowe':
    def bubble_sort(arr):
        for i in range(1, len(arr)):
            for j in range(len(arr) - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


    print(bubble_sort([900000, 432, 6, 3, 4, 63, 123, 456, 34, 5, 4, 534]))
    
if 0 and 'sortowanie przez wybór (python slices)':
    def func(arr):
        result = []
        mindx = 0
        mini = arr[mindx]
        while len(arr) > 1:
            for i, x in enumerate(arr):
                if x < mini:
                    mini = x
                    mindx = i
            result.append(mini)
            arr = arr[:mindx] + arr[mindx + 1:]
            mindx = 0
            mini = arr[mindx]
        return result + arr


    print(func([345678, 9, 8, 7, 6, 5]))
    
if 0 and 'sortowanie przez wstawianie (liniowe)':
    def func(arr):
        for i in range(1, len(arr)):
            while arr[i] < arr[i - 1] and i > 0:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr


    print(func([0, 9, 8, 3, 2, 1]))
    
if 0 and 'sortowanie binarne':
    def binary_sort(arr):
        for i in range(1, len(arr)):
            l, r = -1, i
            while r - l > 1:
                j = (l + r) // 2
                if arr[j] >= arr[i]:
                    if arr[j - 1] <= arr[i]:
                        arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i + 1:]
                        break
                    r = j
                else:
                    l = j
        return arr


    print(binary_sort([9, 10, 2]))
    
if 1 and 'sortowanie kubełkowe':
    def bucket_sort(arr):
        mini = arr[0]
        maxi = arr[0]
        for x in arr:
            maxi = max(x, maxi)
            mini = min(x, mini)

        buckets_len = maxi - mini + 1
        buckets = [0] * buckets_len

        for x in arr:
            buckets[x - mini] += 1

        arr.clear()
        for i in range(buckets_len):
            arr = arr + [i + mini] * buckets[i]
        return arr


    print(bucket_sort([-3,-1,9, 7, 6, 5, 4, 3, 21]))
    
if 0 and 'sortowanie przez scalanie':
    def split(arr):
        if len(arr) <= 1: return arr

        m = len(arr) // 2

        right = []
        left = []

        for x in arr:
            y = arr[m];
            if   y < x: right.append(x)
            elif y > x: left.append(x)
            elif len(left) > len(right): right += [y]
            else: left += [y]

        return merge(split(left), split(right))


    def merge(list1, list2):
        l = min(len(list1), len(list2))

        arr = []

        while list1 and list2:
            if list1[0] <= list2[0]: arr.append(list1.pop(0))
            else: arr.append(list2.pop(0))

        return arr + list1 + list2


    print(split([0, 9, 8, 7, 6, 5, 5679]))
    
if 0 and 'sortowanie szybkie':
    # pivot element biędzie po prawej, bo tak monetka się wylosowała
    def func(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr.pop()
        left_arr = []
        right_arr = []
        for x in arr:
            if pivot < x:
                right_arr.append(x)
            else:
                left_arr.append(x)

        return func(left_arr) + [pivot] + func(right_arr)


    print(func([0, 9, 3, 5, 8, 2, 7]))
    
if 0 and 'maksymalny ciąg jedynek w liczbie dzisietnej, zapisanej dwójkowo':
    def func(n):
        i = 0
        m = 0
        while n > 0:
            if n % 2 == 1:
                i += 1
            else:
                if m < i:
                    m = i
                i = 0
            n //= 2
        return m

    print(func(187))
    
if 0 and 'sortowanie szczytów po lewej stronie w układzie kartezyjskim':
    def func():
        X = [None, -2, -1, -1.2, 3, 4, 3, 2, 5, 7, 6]
        Y = [None, 1, 2, 7, 32, 12, 4, 146, 3, 3, 16]
        n = len(X) - 1
        for i in range(1, n + 1):
            for j in range(1, n - i):
                if X[j] / Y[j] > X[j + 1] / Y[j + 1]:
                    X[j], X[j + 1] = X[j + 1], X[j]
                    Y[j], Y[j + 1] = Y[j + 1], Y[j]
        return [X, Y]

    print(func())

if 0 and 'NWD i NWW':
    def NWD(x, y):
        if x < y: x, y = y, x
        r = x % y
        if r == 0: return y
        return NWD(y, r)

    def NWW(x, y):
        return x,y: x * y // NWD(x,y)
    
    print(NWD(15, 12))
    print(NWW(15, 12))

if 0 and 'szybki pierwiastek Newtona':
    def sqrt(n):
        snd = n/2
        while abs(snd - n/snd) > 0.000001:
            snd = (snd + n/snd)/2
        return round(snd, 6)
    
    print(sqrt(169))

if 0 and 'reverse the number':
    def func1(x):
        result = 0
        z = 1 if x >= 0 else -1
        while z*x > 0:
            result*=10
            result+=x%(10*z)
            x=x//(z*10)//z
        return result
    
    print(func1(-1230))