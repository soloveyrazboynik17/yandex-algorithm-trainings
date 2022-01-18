d = int(input())
X = list(map(int, input().split()))
ans = 0
if X[0] < 0:
    ans = 1 if X[1] <= d / 2 else 3
elif X[1] < 0:
    ans = 1 if X[0] <= d / 2 else 2
elif sum(X) > d:
    ans = 2 if X[0] >= X[1] else 3
print(ans)
