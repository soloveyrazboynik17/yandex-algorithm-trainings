g, s = map(int, input().split())
W = input()
print(len(W))
S = input()
W_d = {}
print(len(S))
for char in W:
    if char not in W_d:
        W_d[char] = 0
    W_d[char] += 1
poss_W_d = {}
n_diffs = 0
for char in S[:g]:
    if char not in poss_W_d:
        poss_W_d[char] = 0
    poss_W_d[char] += 1
    if char not in W_d or poss_W_d[char] > W_d[char]:
        n_diffs += 1
ans = 1 if n_diffs == 0 else 0
for i in range(g, len(S)):
    char_del = S[i-g]
    char_add = S[i]
    if char_del in W_d and poss_W_d[char_del] <= W_d[char_del]:
        n_diffs += 1
    poss_W_d[char_del] -= 1
    if char_add not in poss_W_d:
        poss_W_d[char_add] = 0
    poss_W_d[char_add] += 1
    if char_add in W_d and poss_W_d[char_add] <= W_d[char_add]:
        n_diffs -= 1
    if n_diffs == 0:
        ans += 1
print(ans)
