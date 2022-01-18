N, K = map(int, input().split())
trees = list(map(int, input().split()))
sorts = {}
lc, rc = 0, N-1
p2 = -1
for p1 in range(N-K+1):
    while len(sorts) < K and p2 < N-1:
        p2 += 1
        if trees[p2] not in sorts:
            sorts[trees[p2]] = 0
        sorts[trees[p2]] += 1
    if len(sorts) == K and p2-p1 < rc-lc:
        lc, rc = p1, p2
    sorts[trees[p1]] -= 1
    if sorts[trees[p1]] == 0:
        del sorts[trees[p1]]
print(lc+1, rc+1)
