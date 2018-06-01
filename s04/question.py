def answer(lst):
    count_zero = lst.count(0)
    if count_zero == 1:
        zero_item_index = lst.index(0)
        out = [0 for i in lst]
        A = 1
        for val in lst:
            if val != 0:
                A *= val
        out[zero_item_index] = A
        return out
    elif count_zero > 1:
        return [0 for i in lst]
    else:
        A = 1
        for val in lst:
            A *= val
        return [A/x for x in lst]

inp = [1, 0, 3, 0, 100, 2]

print(answer(inp))