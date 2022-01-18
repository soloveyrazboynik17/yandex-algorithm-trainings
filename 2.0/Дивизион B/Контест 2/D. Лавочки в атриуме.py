L, K = map(int, input().split())
D = list(map(int, input().split()))
center = L // 2
if L % 2 == 1 and center in D:
    print(center)
else:
    if K == 2:
        print(*D)
    else:
        i = 0
        while D[i] < center:
            i += 1
        print(D[i-1], D[i])
