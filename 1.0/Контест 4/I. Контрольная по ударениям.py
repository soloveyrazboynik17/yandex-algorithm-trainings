def number_of_stresses(word):
    count = 0
    for char in word:
        if char.isupper():
            count += 1
    return count


N = int(input())
d = {}
for _ in range(N):
    word = input()
    word_lc = word.lower()
    if word_lc not in d:
        d[word_lc] = []
    d[word_lc].append(word)
n_mistakes = 0
for word in input().split():
    word_lc = word.lower()
    n_stresses = number_of_stresses(word)
    if n_stresses == 0 or n_stresses > 1:
        n_mistakes += 1
    elif word_lc in d and word not in d[word_lc]:
        n_mistakes += 1
print(n_mistakes)
