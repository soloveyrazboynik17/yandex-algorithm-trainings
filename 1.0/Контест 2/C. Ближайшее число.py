N = int(input())
L = list(map(int, input().split()))
x = int(input())
ans = L[0]
for i in range(1, len(L)):
    if abs(L[i] - x) < abs(ans - x):
        ans = L[i]
print(ans)
