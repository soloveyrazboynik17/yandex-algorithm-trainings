N, M = map(int, input().split())
anya_cubes = set()
borya_cubes = set()
for _ in range(N):
    anya_cubes.add(int(input()))
for _ in range(M):
    borya_cubes.add(int(input()))
both = anya_cubes & borya_cubes
only_anya = anya_cubes - both
only_borya = borya_cubes - both
print(len(both))
print(*sorted(both))
print(len(only_anya))
print(*sorted(only_anya))
print(len(only_borya))
print(*sorted(only_borya))
