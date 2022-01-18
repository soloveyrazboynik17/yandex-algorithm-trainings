def numberOfSegemnts(segment_len, L):
    count = 0
    for i in range(len(L)):
        count += L[i] // segment_len
    return count


N, K = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
l, r = 0, max(L)
while l < r:
    segment_len = (l + r + 1) // 2
    if numberOfSegemnts(segment_len, L) >= K:
        l = segment_len
    else:
        r = segment_len - 1
print(l)
