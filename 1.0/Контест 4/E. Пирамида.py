N = int(input())
blocks = {}
for _ in range(N):
    w, h = map(int, input().split())
    if w not in blocks:
        blocks[w] = []
    blocks[w].append(h)
ans = 0
for w in blocks:
    ans += max(blocks[w])
print(ans)
