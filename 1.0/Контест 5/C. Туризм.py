def prefix_heights(diffs):
    prefix_heights = [0] * (N+1)
    for i in range(1, N + 1):
        if diffs[i-1] <= 0:
            prefix_heights[i] = prefix_heights[i-1]
        else:
            prefix_heights[i] = prefix_heights[i-1] + diffs[i-1]
    return prefix_heights


N = int(input())
heights = []
for _ in range(N):
    x, y = map(int, input().split())
    heights.append(y)
diffs = [heights[0]]
for i in range(1, N):
    diffs.append(heights[i]-heights[i-1])
lr_prefix_heights = prefix_heights(diffs)
rl_prefix_heights = prefix_heights(list(map(lambda x: -x, diffs)))
M = int(input())
for _ in range(M):
    s, f = map(int, input().split())
    if s < f:
        print(lr_prefix_heights[f]-lr_prefix_heights[s])
    else:
        print(rl_prefix_heights[s]-rl_prefix_heights[f])
