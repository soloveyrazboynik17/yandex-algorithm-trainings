import sys

d = {}
ans = []
words = sys.stdin.read().split()
for word in words:
    if word not in d:
        d[word] = 0
    ans.append(d[word])
    d[word] += 1
print(' '.join(map(str, ans)))
