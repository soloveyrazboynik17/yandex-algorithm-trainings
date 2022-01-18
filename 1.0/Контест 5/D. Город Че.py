n, r = map(int, input().split())
distances = list(map(int, input().split()))
p1, p2 = 0, 0
n_pairs = 0
while p2 < n:
    m_diff = distances[p2] - distances[p1]
    if m_diff > r:
        n_pairs += n-p2
        p1 += 1
    else:
        p2 += 1
print(n_pairs)
