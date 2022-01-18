import sys

d = {}
words = sys.stdin.read().split()
for word in words:
    if word not in d:
        d[word] = 0
    d[word] += 1
max_value = max(d.values())
ans = min([key for key, value in d.items() if value == max_value])
print(ans)
