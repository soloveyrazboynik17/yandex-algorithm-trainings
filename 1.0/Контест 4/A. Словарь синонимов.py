N = int(input())
d = {}
for _ in range(N):
    synonym1, synonym2 = input().split()
    d[synonym1] = synonym2
    d[synonym2] = synonym1
synonym = input()
print(d[synonym])
