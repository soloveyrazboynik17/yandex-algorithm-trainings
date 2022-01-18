n, k = map(int, input().split())
s = input()
length, idx = 0, 0
d = {}
p1, p2 = 0, 0
for p1 in range(len(s)):
    while p2 < len(s) and (s[p2] not in d or d[s[p2]] < k):
        if s[p2] not in d:
            d[s[p2]] = 0
        d[s[p2]] += 1
        p2 += 1
    if p2 - p1 > length:
        length = p2 - p1
        idx = p1
    d[s[p1]] -= 1
    p1 += 1
print(length, idx+1)
