if 0 and 'list comprehensions':
    # long
    init_each_1 = []
    for i in range(10):
        init_each_1.append(i)

    # exact same, but short
    init_each_2 = [i for i in range(10)]

    # exact same, but even shorter
    init_each_3 = list(range(10))

    print(init_each_1)
    print(init_each_2)
    print(init_each_3)

    # full functionality
    roots = [f"{x}" for x in init_each_2 if x != 3]
    print(f"{roots = }")

    # 2D array x=9, y=4
    arr2d = [list(range(9)) for _ in range(4)]
    print(f"{arr2d = }")

    # slice full array on steps
    step = 3
    size = 9
    arr = list(range(size))
    every3 = [arr[i : i+step] for i in range(0, size, step)]

    print(f"{every3 = }")

if 0 and 'slices':
    py_string = 'Python'

    slice_object = slice(3)
    print(py_string[slice_object])  # Pyt

    slice_object = slice(1, 6, 2)
    print(py_string[slice_object])  # yhn

    slice_list = [1, 2, 3, 4, 5, 6]
    slicer = slice(len(slice_list), 0, -1)
    print(slice_list[slicer])

    kod = "63457KOK"
    print(kod[slice(-3)])  # prints number
    print(kod[slice(5)])  # prints number too

    print(kod[slice(5, len(kod))])  # prints number
    print(kod[slice(-3, len(kod))])  # prints number too

if 0 and 'slices (simplified)':
    srezy = [1, 2, 3, 4, 5, 6]
    print(srezy[::-1])  # show in reversed oreder

    srezy.reverse()  # reverse entire list (for instance)
    print(srezy)

    str_var = '1234'
    print(str_var[::-1])  # show in reversed oreder

    str_var = str_var[::-1]  # reverse entire string (no methods btw)
    print(str_var)

    strin = "12345KOK"
    print(strin[:-3])  # 12345
    print(strin[-3:])  # KOK

if 0 and "for loop":
    arr = [1, 2, 3, 4, 5]
    N = len(arr)
    # for (int i = 0; i < N; i++)
    for i in range(N):
        print(arr[i], end=" ")
    print("\n")
    # for (int i = N - 1; i <= 0; i--) is equal to:
    # for (int i = N - 1; i < -1; i-=1)
    for i in range(N - 1, -1, -1):
        print(arr[i], end=" ")

    # if u don't need to use index in tour loop, write:
    for _ in range(12): pass

if 0 and 'dictionary':
    dic = {"12": 22}

    # find key
    print(dic.__contains__("12"))
    # same thing
    print("12" in dic)

    # comprehension
    # k : v for k (or for k, v, or just v) in iterable
    # k is k and v is 0 in this example
    dic = {k: 0 for k in [1, 2, 3, 4, 5]}

    for i, k in enumerate(dic):
        print(i, k)

    for k, v in dic.items():
        print(k, v)

    for i, (k, v) in enumerate(dic.items()):
        print(i, k, v)

    # wrong code
    """
    for i, k, v in enumerate(dic.items()):
        print(i, k, v)
    """

if 0 and 'Profiling':
    def safe_field():
        import cProfile
        import pstats
        with cProfile.Profile() as pr:
            print("smth")  # function that needs to be analyzed
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()

if 0 and 'Open files':
    def sefe_field():
        with open('liczby.txt', 'r') as f:
            file = [int(x.replace("\n", "")) for x in f.readlines()]
    # or
    def sefe_field2():
        file = [int(x.replace("\n", "")) for x in open('liczby.txt', 'r').readlines()]

if 0 and 'for loop, use enumerate()':
    arr = ["a", "b", "c", "d", "e"]
    # usually you do:
    for i in range(len(arr)):
        print("index:", i, "value:", arr[i])
    # use this instead:
    for i, x in enumerate(arr):
        print("index:", i, "value:", x)

if 0 and '* of docstring (cool wide text)':
    def smth(n):
        print(*n)


    smth('''Don't even think about it...''')

if 0 and 'filter() function':
    def some_sort(v): return x % 2 == 1

    guanan = list(filter(some_sort, [1, 2, 3, 4, 5, 6, 7, 8]))
    # or use lambda
    guanan = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8]))

    print(guanan)

if 0 and 'map() function':
    def some_sort(v):
        return v * 2


    guanan = list(map(some_sort, [1, 2, 3, 4, 5, 6, 7, 8]))  # or lambda
    print(guanan)
    
if 0 and 'randint() function':
    def safe_field():
        from random import randint
        print(randint(1, 10))


    safe_field()

