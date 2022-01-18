N = int(input())
X = set()
for _ in range(N):
    x, y = map(int, input().split())
    if x not in X:
        X.add(x)
print(len(X))
