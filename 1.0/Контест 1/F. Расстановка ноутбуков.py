n1_s1, n1_s2, n2_s1, n2_s2 = map(int, input().split())
n1 = [n1_s1, n1_s2]
n2 = [n2_s1, n2_s2]
table = []
for i in range(len(n1)):
    for j in range(len(n2)):
        s1 = max(n1[i], n2[j])
        s2 = n1[i-1] + n2[j-1]
        if not table or table[0]*table[1] > s1*s2:
            table = [s1, s2]
print(*table)
