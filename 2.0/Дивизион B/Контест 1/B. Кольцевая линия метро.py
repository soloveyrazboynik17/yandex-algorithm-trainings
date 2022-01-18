N, i, j = map(int, input().split())
if i > j:
    i, j = j, i
print(min(j - i - 1, N - j - 1 + i))
