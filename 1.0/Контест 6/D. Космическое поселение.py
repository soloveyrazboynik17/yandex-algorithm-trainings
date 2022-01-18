n, a, b, w, h = map(int, input().split())
l, r = 0, w * h // n
while l < r:
    d = (l + r + 1) // 2
    if (w // (a + 2 * d)) * (h // (b + 2 * d)) >= n or \
            (h // (a + 2 * d)) * (w // (b + 2 * d)) >= n:
        l = d
    else:
        r = d - 1
print(l)
