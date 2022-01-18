at_least_one_knows = set()
all_know = set()
N = int(input())
for i in range(N):
    M = int(input())
    all_know_i = set()
    for _ in range(M):
        language = input()
        if i == 0:
            all_know_i.add(language)
        elif language in all_know:
            all_know_i.add(language)
        at_least_one_knows.add(language)
    all_know = all_know_i
print(len(all_know))
print('\n'.join(all_know))
print(len(at_least_one_knows))
print('\n'.join(at_least_one_knows))
