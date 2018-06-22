a = 1
b = 0
lst = [1, 2]
try:
    print(lst[3])
    c = a / b
    print(c)
except ZeroDivisionError:
    print('something went wrong with a/b ')
except IndexError:
    print('index error')

