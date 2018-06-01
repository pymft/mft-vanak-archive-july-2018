f = open('wasteland.txt', 'r')

# read r
# write w
# append a

text = f.read()
lines = text.split('\n')

for i, line in enumerate(lines):
    print(i, line)


#
# get a list of words  : words
#
# list of unique words : unique_words
#
# dict -- word: occurances
#