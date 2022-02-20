import sys

election = []
for line in sys.stdin:
    line = line.split()
    party_name = ' '. join(line[:-1])
    n_votes = int(line[-1])
    election.append([party_name, n_votes])

total_votes = 0
for party in election:
    total_votes += party[1]

fep = total_votes / 450
for i in range(len(election)):
    n_places = election[i][1] / fep
    election[i].extend([int(n_places), n_places - int(n_places)])

total_votes_new = 0
for party in election:
    total_votes_new += party[2]

election_sorted = sorted(election, key=lambda a: (a[3], a[2]), reverse=True)
i = 0
while total_votes_new + i < 450:
    election_sorted[i][2] += 1
    i += 1

for party in election:
    print(party[0], party[2])
