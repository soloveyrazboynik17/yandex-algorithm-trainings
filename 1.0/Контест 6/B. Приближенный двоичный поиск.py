def findNearest(n, seq):
    l, r = 0, len(seq) - 1
    while r - l > 1:
        m = (l + r) // 2
        if n <= seq[m]:
            r = m
        else:
            l = m
    if seq[r] - n < n - seq[l]:
        return seq[r]
    return seq[l]


N, K = map(int, input().split())
seq1 = sorted(map(int, input().split()))
for n in map(int, input().split()):
    print(findNearest(n, seq1))
