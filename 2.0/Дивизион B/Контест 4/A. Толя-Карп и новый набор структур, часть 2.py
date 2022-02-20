n = int(input())
ans = {}
while n != 0:
    d_i, a_i = map(int, input().split())
    if d_i not in ans:
        ans[d_i] = 0
    ans[d_i] += a_i
    n -= 1
for d_i in sorted(ans.keys()):
    print(d_i, ans[d_i])
