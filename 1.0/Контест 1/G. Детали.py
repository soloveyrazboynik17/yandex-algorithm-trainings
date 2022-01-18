N, K, M = map(int, input().split())
ans = 0
while N >= K >= M:
    ans += (N // K) * (K // M)
    N = (N % K) + (K % M) * (N // K)
print(ans)
