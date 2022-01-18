N = int(input())
turtles = set()
for _ in range(N):
    a, b = map(int, input().split())
    if a >= 0 and b >= 0 and a+b == N-1:
        turtles.add((a, b))
print(len(turtles))
