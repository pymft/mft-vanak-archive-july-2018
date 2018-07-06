lst = [1, 2, 80, 21, 212, 100, 21]

print(lst, id(lst))
lst.sort()
print(lst, id(lst))

lst2 = [1, 2, 80, 21, 212, 100, 21]
print("lst2 before calling sorted function", lst2, id(lst2))
lst2_sorted = sorted(lst2)
print("lst2 before calling sorted function", lst2, id(lst2))
print("returned value --> ", lst2_sorted, id(lst))