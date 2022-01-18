n = int(input())
max, max_count = n, 0
while n != 0:
    if n > max:
        max, max_count = n, 1
    elif n == max:
        max_count += 1
    n = int(input())
print(max_count)
