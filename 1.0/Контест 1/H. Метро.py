a = int(input())
b = int(input())
n = int(input())
m = int(input())
time = []
for i in range(3):
    platform1_time = a*(n-1+i) + n
    for j in range(3):
        platform2_time = b*(m-1+j) + m
        if i == j == 0:
            if platform2_time == platform1_time:
                time.append(platform2_time)
        elif i == 0:
            if 0 <= platform2_time - platform1_time <= a:
                time.append(platform1_time)
        elif j == 0:
            if 0 <= platform1_time - platform2_time <= b:
                time.append(platform2_time)
        elif 0 <= platform2_time - platform1_time <= b:
            time.append(platform1_time)
        elif 0 <= platform1_time - platform2_time <= a:
            time.append(platform2_time)
if not time:
    print(-1)
else:
    print(min(time), max(time))
