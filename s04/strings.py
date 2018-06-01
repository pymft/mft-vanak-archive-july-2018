text = "all work and no play makes Jack a dull boy"

res = text.find('Jack')

print(res)

lst = [1, 2, 3]
lst.append(10)
lst = lst + [1]
val_of_removed_item = lst.pop(1)
print(val_of_removed_item, lst)

dct = {'a': 1, 'b':10}
print(dct, id(dct))
dct.update({'c': 10})
print(dct, id(dct))
