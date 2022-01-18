n = int(input())
results = list(map(int, input().split()))
winner = (0, results[0])
for i in range(1, n):
    if results[i] > winner[1]:
        winner = (i, results[i])
if winner[0] + 1 == n:
    print(0)
else:
    Vasya = None
    for i in range(winner[0]+1, n-1):
        if (results[i] % 10 == 5 and results[i] > results[i+1]) and (Vasya is None or results[i] > Vasya[1]):
            Vasya = (i, results[i])
    if Vasya is None:
        print(0)
    else:
        k = 0
        for i in range(n):
            if results[i] > Vasya[1]:
                k += 1
        print(k+1)
