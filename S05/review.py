# decorator

def my_function(out):
    def inner():
        return out

    return inner

# 0x03A18E40
# 0x02FF8E40

echoed_val = 'Salut'
returned_function = my_function(echoed_val)
res_of_returned_function = returned_function()

print(res_of_returned_function)


