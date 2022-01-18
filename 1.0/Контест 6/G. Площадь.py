n = int(input())
m = int(input())
t = int(input())
l, r = 0, (min(n, m) - 1) // 2
while l < r:
    width = (l + r + 1) // 2
    if 0 < n * m - (n - 2 * width) * (m - 2 * width) <= t:
        l = width
    else:
        r = width - 1
print(l)
