b = list(map(int, input().split()))
h_idxs = []
s_idxs = []
for i in range(len(b)):
    if b[i] == 1:
        h_idxs.append(i)
    elif b[i] == 2:
        s_idxs.append(i)
i = 0
max_d = 0
for h_idx in h_idxs:
    while h_idx > s_idxs[i] and i < len(s_idxs) - 1:
        i += 1
    d = 0
    if h_idx > s_idxs[i]:
        d = h_idx - s_idxs[i]
    elif i == 0:
        d = s_idxs[i] - h_idx
    elif s_idxs[i-1] < h_idx < s_idxs[i]:
        d = min(s_idxs[i] - h_idx, h_idx - s_idxs[i-1])
    if d > max_d:
        max_d = d
print(max_d)
