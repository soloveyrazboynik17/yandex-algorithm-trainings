r = int(input())
i = int(input())
c = int(input())
final_verdict = i
if i == 0:
    final_verdict = 3 if r != 0 else c
elif i == 1:
    final_verdict = c
elif i == 4:
    final_verdict = 3 if r != 0 else 4
elif i == 6:
    final_verdict = 0
elif i == 7:
    final_verdict = 1
print(final_verdict)
