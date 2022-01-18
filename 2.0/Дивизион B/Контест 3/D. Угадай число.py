n = int(input())
probable_numbers = set(range(1, n+1))
s = input()
while s != 'HELP':
    guess = set(map(int, s.split()))
    ans = input()
    if ans == 'YES':
        probable_numbers &= guess
    else:
        probable_numbers -= guess
    s = input()
print(*sorted(probable_numbers))
