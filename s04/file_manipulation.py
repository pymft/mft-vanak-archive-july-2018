f = open('wasteland.txt', 'r')

# read r
# write w
# append a

text = f.read()
lines = text.split('\n')

for i, line in enumerate(lines):
    print(i, line)
