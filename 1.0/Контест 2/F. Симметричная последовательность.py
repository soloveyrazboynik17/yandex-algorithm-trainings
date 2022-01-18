N = int(input())
seq = list(map(int, input().split()))
to_add = []
left, right = 0, N-1
last = left
while left < right:
    if seq[left] == seq[right]:
        left += 1
        right -= 1
    else:
        if left - last > 1:
            right += left - last - 1
            left = last + 1
        to_add.append(seq[left])
        last = left
        left += 1
print(len(to_add))
print(*to_add[::-1])