from math import ceil
K1, M, K2, P2, N2 = map(int, input().split())
P1, N1 = 0, 0
n_floors = M*(P2-1) + N2
k_per_floor_min = ceil(K2 / n_floors)
if P2 == N2 == 1:
    if K1 < K2:
        P1, N1 = 1, 1
    else:
        if M > 1:
            if K1 > M:
                P1, N1 = 0, 0
            else:
                P1, N1 = 1, 0
        else:
            P1, N1 = 0, 1
elif M < N2:
    P1, N1 = -1, -1
else:
    if 0 <= n_floors*k_per_floor_min - K2 < k_per_floor_min:
        k_per_floor_max = k_per_floor_min + ((K2-1) % k_per_floor_min)//(n_floors-1)
        P1_max = ceil(K1 / (M*k_per_floor_max))
        P1_min = ceil(K1 / (M * k_per_floor_min))
        N1_max = ceil(K1/k_per_floor_max - M*(P1_max-1))
        N1_min = ceil(K1 / k_per_floor_min - M * (P1_min - 1))
        if P1_min == P1_max:
            P1 = P1_min
        else:
            P1 = 0
        if N1_min == N1_max:
            N1 = N1_min
        else:
            N1 = 0
    else:
        P1, N1 = -1, -1
print(P1, N1)
