import sys

# usage
# sample.py -x 10 -y 2 -m div

flags = sys.argv[1:]
x_ind = flags.index('-x')
x = flags[x_ind+1]
x = int(x)
y_ind = flags.index('-y')
y = flags[y_ind+1]
y = int(y)

mode_ind = flags.index('-m')
mode = flags[mode_ind+1]

if mode == 'div':
    print(x/y)
elif mode == 'pow':
    print (x ** y)
elif mode == 'sum':
    print (x + y)
elif mode == 'sub':
    print (x - y)
