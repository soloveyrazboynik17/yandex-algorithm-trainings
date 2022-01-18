import sys

database = {}
for line in sys.stdin:
    info = line.split()
    customer = info[0]
    product = info[1]
    cost = int(info[2])
    if customer not in database:
        database[customer] = {}
    if product not in database[customer]:
        database[customer][product] = 0
    database[customer][product] += cost
for customer in sorted(database):
    print(f'{customer}:')
    for product in sorted(database[customer]):
        print(product, database[customer][product])
