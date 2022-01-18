def get_base_pairs(genome):
    base_pairs = set()
    for i in range(len(genome)-1):
        base_pairs.add(genome[i:i+2])
    return base_pairs


genome1 = input()
genome2 = input()
genome1_base_pairs = get_base_pairs(genome1)
genome2_base_pairs = get_base_pairs(genome2)
both = genome1_base_pairs & genome2_base_pairs
closeness = 0
for i in range(len(genome1)-1):
    if genome1[i:i+2] in both:
        closeness += 1
print(closeness)
