n = int(input())
c_capacity = list(sorted(map(int, input().split())))
m = int(input())
models = {}
for _ in range(m):
    b, c = map(int, input().split())
    if b not in models:
        models[b] = c
    elif c < models[b]:
        models[b] = c
m_capacity = list(sorted(models.keys()))
p2 = len(m_capacity)-1
min_price = models[m_capacity[p2]]
p2 -= 1
min_sum = 0
for p1 in range(n-1, -1, -1):
    while p2 > -1 and c_capacity[p1] <= m_capacity[p2]:
        if models[m_capacity[p2]] < min_price:
            min_price = models[m_capacity[p2]]
        p2 -= 1
    min_sum += min_price
print(min_sum)
