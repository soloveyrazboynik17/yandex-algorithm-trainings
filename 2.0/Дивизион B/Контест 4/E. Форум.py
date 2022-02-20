N = int(input())
i = 1
messages = {}
while N != 0:
    n = int(input())
    if n == 0:
        theme = input()
        message = input()
        messages[i] = theme
    else:
        message = input()
        messages[i] = messages[n]
    i += 1
    N -= 1
stats = {}
for theme in messages.values():
    if theme not in stats:
        stats[theme] = 0
    stats[theme] += 1
print(max(stats, key=stats.get))
