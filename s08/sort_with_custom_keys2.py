lst = [(1, 2), (3, 100), (6, 10), (1, -10), (-1, 5)]

lst2 = [t[1] for t in lst]
lst3 = map(lambda s: s[1], lst)
print(lst2)


print(lst)
lst.sort(key=lambda s: abs(s[1]-s[0]))
print(lst)