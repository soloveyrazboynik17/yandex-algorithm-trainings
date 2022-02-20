import sys
ans = {}
for line in sys.stdin:
    line = line.split()
    candidate, n_votes = line[0], int(line[1])
    if candidate not in ans:
        ans[candidate] = 0
    ans[candidate] += n_votes
for candidate in sorted(ans.keys()):
    print(candidate, ans[candidate])
