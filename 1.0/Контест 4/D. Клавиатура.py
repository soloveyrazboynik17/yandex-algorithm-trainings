n = int(input())
count = list(map(int, input().split()))
k = int(input())
for key in map(int, input().split()):
    count[key-1] -= 1
for key in range(n):
    if count[key] < 0:
        print('YES')
    else:
        print('NO')
