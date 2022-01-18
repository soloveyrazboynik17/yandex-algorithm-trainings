L = list(map(int, input().split()))
ans = 0
for i in range(1, len(L)-1):
    if L[i-1] < L[i] > L[i+1]:
        ans += 1
print(ans)
