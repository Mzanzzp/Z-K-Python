def total_length(*args):
    a = 0
    for i in args:
        for j in i:
            a += len(j)
    return a


# assert('hello', {'red': 50, 'purple': 100}) == 7
# assert([4, 5], (6, 7)) == 4

a = ([1, 2], "hello", "hello")
b = ('hello', {'red': 50, 'purple': 100})
print(total_length(b))