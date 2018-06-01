f = open('wasteland.txt', 'r')

# read r
# write w
# append a
text = f.read()
f.close()

words = list(text.strip().split())
unique_words = set(words)

res = {item: words.count(item) for item in unique_words}

#                    |<==list==>|
sorted_list = sorted(res.items(), key=lambda x: x[1], reverse=True)


for word, rep in sorted_list[:10]:
    print(word, '--->', rep)

