a = int(input())
b = int(input())
c = int(input())
l, r = 0, 2 * a + b
while l < r:
    d = (l + r) // 2
    if 2 * (2 * a + 3 * b + 4 * c + 5 * d) >= 7 * (a + b + c + d):
        r = d
    else:
        l = d + 1
print(l)
