N, M, K = map(int, input().split())
field = []
for _ in range(N):
    field.append([0]*M)
for _ in range(K):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    field[i][j] = '*'
    for deviation_i in range(-1*((i-1) >= 0), ((i+1) < N) + 1, 1):
        for deviation_j in range(-1*((j-1) >= 0), ((j+1) < M) + 1, 1):
            if field[i+deviation_i][j+deviation_j] != '*':
                field[i+deviation_i][j+deviation_j] += 1
for row in field:
    print(' '.join(map(str, row)))
