left_bound = 30
right_bound = 4000
n = int(input())
prev = float(input())
for i in range(n-1):
    line = input().split()
    f, word = float(line[0]), line[1]
    mean = (prev + f) / 2
    if f < prev:
        if word == 'closer':
            right_bound = min(mean, right_bound)
        elif word == 'further':
            left_bound = max(mean, left_bound)
    elif f > prev:
        if word == 'closer':
            left_bound = max(mean, left_bound)
        elif word == 'further':
            right_bound = min(mean, right_bound)
    prev = f
print(left_bound, right_bound)
