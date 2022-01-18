L = list(map(int, input().split()))
ans = 'YES'
for i in range(1, len(L)):
    if L[i] <= L[i-1]:
        ans = 'NO'
        break
print(ans)
