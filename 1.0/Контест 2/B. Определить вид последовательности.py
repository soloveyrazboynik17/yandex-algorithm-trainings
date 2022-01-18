types = ['CONSTANT', 'ASCENDING', 'WEAKLY ASCENDING',
         'DESCENDING', 'WEAKLY DESCENDING', 'RANDOM ']
types = dict.fromkeys(types, True)
n = int(input())
prev = None
while n != -2*(10**9):
    if prev is not None:
        if n > prev:
            types['CONSTANT'] = False
            types['DESCENDING'] = False
            types['WEAKLY DESCENDING'] = False
        elif n < prev:
            types['CONSTANT'] = False
            types['ASCENDING'] = False
            types['WEAKLY ASCENDING'] = False
        else:
            types['ASCENDING'] = False
            types['DESCENDING'] = False
    prev = n
    n = int(input())
for key in types:
    if types[key]:
        print(key)
        break
