s = input()
tugriks = 0
for i in range(len(s) // 2):
    if s[i] != s[-(i+1)]:
        tugriks += 1
print(tugriks)
