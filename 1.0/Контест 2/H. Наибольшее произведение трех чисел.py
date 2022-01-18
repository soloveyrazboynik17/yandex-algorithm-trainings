def find_max3_min2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    max3 = None
    min1, min2 = max2, max1
    for i in range(2, len(seq)):
        n = seq[i]
        if n >= max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif max1 > n >= max2:
            max3 = max2
            max2 = n
        elif max3 is None or max2 > n > max3:
            max3 = n
        if n <= min1:
            min2, min1 = min1, n
        elif min1 < n < min2:
            min2 = n
    return (max1, max2, max3), (min1, min2)


seq = list(map(int, input().split()))
if len(seq) == 3:
    print(*seq)
else:
    maximums, minimums = find_max3_min2(seq)
    option1 = minimums[0]*minimums[1]*maximums[0]
    option2 = maximums[0]*maximums[1]*maximums[2]
    if option1 > option2:
        print(*minimums, maximums[0])
    else:
        print(*maximums)
