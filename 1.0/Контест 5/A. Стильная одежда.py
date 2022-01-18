N = int(input())
colors1 = list(map(int, input().split()))
M = int(input())
colors2 = list(map(int, input().split()))
color1, color2 = colors1[0], colors2[0]
p2 = 1 if color1 >= color2 else 0
for p1 in range(N):
    while p2 < M-1 and colors1[p1] > colors2[p2]:
        p2 += 1
    if abs(color1-color2) > abs(colors1[p1]-colors2[p2]):
        color1 = colors1[p1]
        color2 = colors2[p2]
    if abs(color1-color2) > abs(colors1[p1] - colors2[p2-1]):
        color1 = colors1[p1]
        color2 = colors2[p2-1]
print(color1, color2)
