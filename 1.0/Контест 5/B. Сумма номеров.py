N, K = map(int, input().split())
nums = list(map(int, input().split()))
prefixsum = [0]*(N+1)
for i in range(1, N+1):
    prefixsum[i] = prefixsum[i-1] + nums[i-1]
p1, p2 = 0, 1
ans = 0
while p2 < N+1:
    diff = prefixsum[p2] - prefixsum[p1]
    if diff == K:
        ans += 1
        p1 += 1
        p2 += 1
    elif diff < K:
        p2 += 1
    elif diff > K:
        p1 += 1
print(ans)
