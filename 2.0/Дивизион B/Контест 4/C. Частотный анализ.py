import sys
words_d = {}
for line in sys.stdin:
    words = line.split()
    for word in words:
        if word not in words_d:
            words_d[word] = 0
        words_d[word] += 1
for word, count in sorted(words_d.items(), key=lambda t: (-t[1], t[0])):
    print(word)
