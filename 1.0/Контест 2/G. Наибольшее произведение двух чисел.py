numbers = list(map(int, input().split()))
max1 = max(numbers[0], numbers[1])
max2 = min(numbers[0], numbers[1])
min1, min2 = max2, max1
for i in range(2, len(numbers)):
    n = numbers[i]
    if n >= max1:
        max2, max1 = max1, n
    elif max2 < n < max1:
        max2 = n
    elif n <= min1:
        min2, min1 = min1, n
    elif min1 < n < min2:
        min2 = n
if max1*max2 > min1*min2:
    print(max2, max1)
else:
    print(min1, min2)
